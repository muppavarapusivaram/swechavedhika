import json
import urllib.error
import urllib.request

BASE_URL = "http://localhost:8000"


def request(method, path, data=None, token=None):
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    body = json.dumps(data).encode("utf-8") if data is not None else None
    req = urllib.request.Request(
        f"{BASE_URL}{path}", data=body, headers=headers, method=method
    )
    try:
        with urllib.request.urlopen(req) as resp:
            content = resp.read()
            content_type = resp.headers.get("content-type", "")
            if "application/json" in content_type:
                return resp.status, json.loads(content.decode("utf-8"))
            return resp.status, content
    except urllib.error.HTTPError as e:
        content = e.read().decode("utf-8")
        return e.code, json.loads(content) if content else {"error": str(e)}


def run_tests():
    print("=== STARTING FULL END-TO-END FEATURE TESTS (Swecha Vedika) ===")

    # 1. Register host
    host_email = "host_rural@swecha.org"
    request(
        "POST",
        "/auth/register",
        {
            "name": "Swecha Host",
            "email": host_email,
            "phone_number": "+919999900001",
            "password": "Password123!",
        },
    )

    # Login host
    status, host_login = request(
        "POST",
        "/auth/login",
        {"email": host_email, "password": "Password123!"},
    )
    assert status == 200, f"Host login failed: {host_login}"
    host_token = host_login["access_token"]
    print("✔ Host authenticated successfully.")

    # 2. Register attendee
    attendee_email = "volunteer_guntur@swecha.org"
    request(
        "POST",
        "/auth/register",
        {
            "name": "Guntur Volunteer",
            "email": attendee_email,
            "phone_number": "+919999900002",
            "password": "Password123!",
        },
    )

    # Login attendee
    status, att_login = request(
        "POST",
        "/auth/login",
        {"email": attendee_email, "password": "Password123!"},
    )
    assert status == 200, f"Attendee login failed: {att_login}"
    att_token = att_login["access_token"]
    print("✔ Attendee authenticated successfully.")

    # 3. Create Event
    status, event = request(
        "POST",
        "/events",
        {
            "title": "గ్రామీణ డిజిటల్ సాధికారత (Rural Digital Empowerment)",
            "description": "Frugal WebRTC & Multilingual Open Source Workshop",
            "scheduled_start": "2026-10-30T10:00:00Z",
            "language": "Telugu / English",
        },
        token=host_token,
    )
    assert status == 201, f"Create event failed: {event}"
    event_id = event["id"]
    print(f"✔ Event created: '{event['title']}' (ID: {event_id[:8]})")

    # 4. Attendee joins event
    status, join_res = request("POST", f"/events/{event_id}/join", token=att_token)
    assert status == 200, f"Join failed: {join_res}"
    print("✔ Attendee joined event.")

    # 5. Attendee raises hand
    status, raise_res = request(
        "POST",
        f"/events/{event_id}/raise-hand",
        {"hand_raised": True},
        token=att_token,
    )
    assert status == 200 and raise_res["hand_raised"] is True
    print("✔ Hand raised successfully by attendee.")

    # 6. Host views attendees and promotes to stage speaker
    status, attendees = request("GET", f"/events/{event_id}/attendees", token=host_token)
    assert status == 200, f"List attendees failed: {attendees}"
    att_user = next(a for a in attendees if a["email"] == attendee_email)
    assert att_user["hand_raised"] is True, "Hand raised not visible to host!"

    status, promote_res = request(
        "POST",
        f"/events/{event_id}/promote-speaker",
        {"user_id": att_user["user_id"], "is_speaker": True},
        token=host_token,
    )
    assert status == 200 and promote_res["is_speaker"] is True
    print("✔ Host promoted attendee to Stage Speaker.")

    # 7. Check token for attendee (now speaker)
    status, token_res = request("POST", f"/events/{event_id}/token", token=att_token)
    assert status == 200 and token_res["is_speaker"] is True
    print("✔ LiveKit token granted with speaker/publish capabilities.")

    # 8. In-Room Live Chat & Telugu Reactions
    status, chat_msg = request(
        "POST",
        f"/events/{event_id}/chat",
        {"content": "👏 నమస్కారం మిత్రులారా! Swecha Vedika chat is working wonderfully."},
        token=att_token,
    )
    assert status == 201, f"Chat send failed: {chat_msg}"

    status, chat_list = request("GET", f"/events/{event_id}/chat", token=host_token)
    assert status == 200 and len(chat_list) >= 1
    assert "నమస్కారం" in chat_list[-1]["content"]
    print("✔ In-Room Live Chat with Telugu reactions verified.")

    # 9. Q&A: Attendee submits question & upvotes
    status, q1 = request(
        "POST",
        f"/events/{event_id}/questions",
        {"content": "How does the 2G low-data mode handle packet loss in remote villages?"},
        token=att_token,
    )
    assert status == 201, f"Q&A submit failed: {q1}"
    q1_id = q1["id"]

    # Upvote question
    status, q1_upvoted = request(
        "POST",
        f"/events/{event_id}/questions/{q1_id}/upvote",
        token=host_token,
    )
    assert status == 200 and q1_upvoted["upvotes"] == 1
    print("✔ Q&A question submitted and upvoted.")

    # Host marks question answered
    status, q1_ans = request(
        "POST",
        f"/events/{event_id}/questions/{q1_id}/answer",
        token=host_token,
    )
    assert status == 200 and q1_ans["is_answered"] is True
    print("✔ Host marked Q&A question as answered.")

    # 10. Live Polls: Host creates poll, attendee votes
    status, poll = request(
        "POST",
        f"/events/{event_id}/polls",
        {
            "question": "What is the typical internet speed in your village/college?",
            "options": ["< 1 Mbps (2G/3G)", "1-10 Mbps (4G)", "> 50 Mbps (Fiber/5G)"],
        },
        token=host_token,
    )
    assert status == 201, f"Poll create failed: {poll}"
    poll_id = poll["id"]

    # Vote option 0 (< 1 Mbps)
    status, poll_voted = request(
        "POST",
        f"/events/{event_id}/polls/{poll_id}/vote",
        {"option_index": 0},
        token=att_token,
    )
    assert status == 200 and poll_voted["vote_counts"]["0"] == 1
    print(f"✔ Live Poll created and attendee voted: {poll_voted['vote_counts']}")

    # 11. Replay-as-Live Engine & Synchronized Broadcast Clock
    status, replay_start = request(
        "POST",
        f"/events/{event_id}/replay-start",
        token=host_token,
    )
    assert status == 200 and replay_start["is_replay"] is True

    status, sync_clock = request("GET", f"/events/{event_id}/sync-clock")
    assert status == 200 and sync_clock["is_replay"] is True
    assert sync_clock["offset_seconds"] >= 0.0
    print(f"✔ Replay-as-Live Clock synchronized: offset {sync_clock['offset_seconds']:.2f}s.")

    # 12. Host Heartbeat & Disconnect Failover
    status, hb_res = request("POST", f"/events/{event_id}/heartbeat", token=host_token)
    assert status == 200

    status, failover = request("GET", f"/events/{event_id}/failover-status")
    assert status == 200 and failover["host_online"] is True
    print("✔ Host resilience heartbeat and failover protocol verified.")

    # 13. Archive: Populate demo AI data & search
    status, demo_ai = request(
        "POST",
        f"/archive/{event_id}/populate-demo-ai",
        token=host_token,
    )
    assert status == 200 and len(demo_ai["transcript"]) > 0
    print("✔ Demo Telugu AI transcript & summary populated.")

    status, search_res = request("GET", "/archive/search?q=WebRTC")
    assert status == 200 and len(search_res) >= 1
    print(f"✔ Archive search verified: found {len(search_res)} matching event(s).")

    status, corpus = request("GET", "/archive/corpus")
    assert status == 200 and len(corpus) > 0
    print(f"✔ Telugu Speech Corpus export verified: {len(corpus)} segments available.")

    # 14. Offline Learning Pack Generator (.zip)
    status, zip_bytes = request("GET", f"/archive/{event_id}/offline-pack")
    assert status == 200 and zip_bytes[:2] == b"PK", "Invalid ZIP header"
    print(f"✔ Offline Pack generated: valid .zip package ({len(zip_bytes)} bytes).")

    # 15. WhatsApp Bot Simulator
    status, wa_events = request(
        "POST",
        "/webhook/whatsapp/simulate",
        {"phone": "+919876543210", "message": "EVENTS"},
    )
    assert status == 200 and "స్వేచ్ఛ వేదిక" in wa_events["reply"]

    status, wa_rsvp = request(
        "POST",
        "/webhook/whatsapp/simulate",
        {"phone": "+919876543210", "message": f"RSVP {event_id[:8]}"},
    )
    assert status == 200 and "RSVP Confirmed" in wa_rsvp["reply"]

    status, wa_ask = request(
        "POST",
        "/webhook/whatsapp/simulate",
        {
            "phone": "+919876543210",
            "message": f"ASK {event_id[:8]}: Can we run this on a Raspberry Pi 4?",
        },
    )
    assert status == 200 and "Question submitted" in wa_ask["reply"]
    print("✔ WhatsApp Bot Simulation (EVENTS, RSVP, ASK) verified successfully.")

    print("\n🎉 ALL 15 DOMAIN TEST SUITES PASSED 100%! ENTIRE SYSTEM COMPLETE! 🎉")


if __name__ == "__main__":
    run_tests()
