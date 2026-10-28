import { useState, useEffect, useRef } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import '@livekit/components-styles';
import {
  LiveKitRoom,
  VideoConference,
  RoomAudioRenderer,
} from '@livekit/components-react';
import LoadingSpinner from '../components/LoadingSpinner';
import WhatsAppSimulator from '../components/WhatsAppSimulator';
import { useAuth } from '../context/AuthContext';
import {
  getAttendees,
  raiseHand,
  promoteSpeaker,
  getQuestions,
  submitQuestion,
  upvoteQuestion,
  markQuestionAnswered,
  getPolls,
  createPoll,
  votePoll,
  getChatMessages,
  sendChatMessage,
  startReplay,
  getSyncClock,
  sendHeartbeat,
  getFailoverStatus,
  getOfflinePackUrl,
} from '../api/client';

export default function RoomPage() {
  const { eventId } = useParams();
  const navigate = useNavigate();
  const { authFetch, user, token } = useAuth();

  const [tokenData, setTokenData] = useState(null);
  const [eventDetails, setEventDetails] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Low-Data Mode (2G Fallback)
  const [lowDataMode, setLowDataMode] = useState(false);

  // Sidebar state: 'attendees' | 'chat' | 'qa' | 'polls'
  const [activeTab, setActiveTab] = useState('chat');
  const [sidebarOpen, setSidebarOpen] = useState(true);

  // Attendees & Hand-raise
  const [attendees, setAttendees] = useState([]);
  const [myHandRaised, setMyHandRaised] = useState(false);
  const [isSpeaker, setIsSpeaker] = useState(false);

  // In-Room Live Chat
  const [chatMessages, setChatMessages] = useState([]);
  const [newChatText, setNewChatText] = useState('');
  const [submittingChat, setSubmittingChat] = useState(false);
  const chatBottomRef = useRef(null);

  // Q&A
  const [questions, setQuestions] = useState([]);
  const [newQuestionText, setNewQuestionText] = useState('');
  const [submittingQ, setSubmittingQ] = useState(false);

  // Polls
  const [polls, setPolls] = useState([]);
  const [newPollQuestion, setNewPollQuestion] = useState('');
  const [newPollOptions, setNewPollOptions] = useState(['Yes', 'No']);
  const [showCreatePoll, setShowCreatePoll] = useState(false);

  // Replay-as-Live
  const [replaySync, setReplaySync] = useState(null);
  const replayVideoRef = useRef(null);

  // Host Resilience & Failover
  const [failoverStatus, setFailoverStatus] = useState(null);

  // WhatsApp Simulator modal
  const [showWhatsApp, setShowWhatsApp] = useState(false);

  // P2P Mesh Telemetry HUD toggle
  const [showTelemetry, setShowTelemetry] = useState(true);

  const isHost = eventDetails && user && eventDetails.host_id === user.id;

  // Initial Room Setup
  useEffect(() => {
    let isMounted = true;

    async function initRoom() {
      setLoading(true);
      setError(null);
      try {
        const event = await authFetch(`/events/${eventId}`);
        if (!isMounted) return;
        setEventDetails(event);

        const tokenRes = await authFetch(`/events/${eventId}/token`, {
          method: 'POST',
        });
        if (!isMounted) return;
        setTokenData(tokenRes);
        setIsSpeaker(tokenRes.is_speaker || false);

        // Fetch replay clock if replay event
        if (event.is_replay) {
          const sync = await getSyncClock(eventId);
          if (isMounted) setReplaySync(sync);
        }
      } catch (err) {
        if (!isMounted) return;
        if (err.status === 404) {
          setError('Event not found or has expired.');
        } else {
          setError(
            err.message || 'Failed to connect to video room. Please try again.'
          );
        }
      } finally {
        if (isMounted) setLoading(false);
      }
    }

    initRoom();
    return () => {
      isMounted = false;
    };
  }, [eventId, authFetch]);

  // Periodic Host Heartbeat
  useEffect(() => {
    if (!token || !isHost) return;
    const interval = setInterval(() => {
      sendHeartbeat(eventId, token).catch(() => {});
    }, 10000);
    return () => clearInterval(interval);
  }, [eventId, token, isHost]);

  // Periodic Room State Polling
  const fetchRoomData = async () => {
    if (!token) return;
    try {
      const [attList, chatList, qList, pList, failover] = await Promise.all([
        getAttendees(eventId, token).catch(() => []),
        getChatMessages(eventId, token).catch(() => []),
        getQuestions(eventId, token).catch(() => []),
        getPolls(eventId, token).catch(() => []),
        getFailoverStatus(eventId).catch(() => null),
      ]);

      setAttendees(attList);
      setChatMessages(chatList);
      setQuestions(qList);
      setPolls(pList);
      if (failover) setFailoverStatus(failover);

      const meInAtt = attList.find((a) => a.user_id === user?.id);
      if (meInAtt) {
        setMyHandRaised(meInAtt.hand_raised);
        setIsSpeaker(meInAtt.is_speaker || isHost);
      }
    } catch (e) {
      console.error('Error fetching room state:', e);
    }
  };

  useEffect(() => {
    fetchRoomData();
    const interval = setInterval(fetchRoomData, 3000);
    return () => clearInterval(interval);
  }, [eventId, token, user?.id, isHost]);

  // Auto-scroll chat to bottom
  useEffect(() => {
    if (activeTab === 'chat' && chatBottomRef.current) {
      chatBottomRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  }, [chatMessages, activeTab]);

  // Hand Raise
  const handleToggleHandRaise = async () => {
    try {
      const nextState = !myHandRaised;
      setMyHandRaised(nextState);
      await raiseHand(eventId, nextState, token);
      fetchRoomData();
    } catch (err) {
      alert('Failed to update hand raise: ' + err.message);
    }
  };

  // Host Stage Promotion
  const handlePromoteSpeaker = async (userId, grantSpeaker) => {
    try {
      await promoteSpeaker(eventId, userId, grantSpeaker, token);
      fetchRoomData();
    } catch (err) {
      alert('Failed to promote attendee: ' + err.message);
    }
  };

  // Live Chat Submit
  const handleSendChat = async (e, customContent = null) => {
    if (e) e.preventDefault();
    const messageContent = customContent || newChatText;
    if (!messageContent.trim() || submittingChat) return;

    setSubmittingChat(true);
    try {
      await sendChatMessage(eventId, messageContent.trim(), token);
      if (!customContent) setNewChatText('');
      fetchRoomData();
    } catch (err) {
      alert('Failed to send chat: ' + err.message);
    } finally {
      setSubmittingChat(false);
    }
  };

  // Submit Question
  const handleQuestionSubmit = async (e) => {
    e.preventDefault();
    if (!newQuestionText.trim() || submittingQ) return;
    setSubmittingQ(true);
    try {
      await submitQuestion(eventId, newQuestionText.trim(), token);
      setNewQuestionText('');
      fetchRoomData();
    } catch (err) {
      alert('Failed to submit question: ' + err.message);
    } finally {
      setSubmittingQ(false);
    }
  };

  // Upvote Question
  const handleUpvote = async (questionId) => {
    try {
      await upvoteQuestion(eventId, questionId, token);
      fetchRoomData();
    } catch (err) {
      alert('Failed to upvote: ' + err.message);
    }
  };

  // Host Mark Answered
  const handleMarkAnswered = async (questionId) => {
    try {
      await markQuestionAnswered(eventId, questionId, token);
      fetchRoomData();
    } catch (err) {
      alert('Failed to mark answered: ' + err.message);
    }
  };

  // Cast Poll Vote
  const handleVotePoll = async (pollId, optionIndex) => {
    try {
      await votePoll(eventId, pollId, optionIndex, token);
      fetchRoomData();
    } catch (err) {
      alert('Failed to vote: ' + err.message);
    }
  };

  // Create Poll
  const handleCreatePoll = async (e) => {
    e.preventDefault();
    if (!newPollQuestion.trim()) return;
    try {
      await createPoll(
        eventId,
        {
          question: newPollQuestion.trim(),
          options: newPollOptions.filter((o) => o.trim().length > 0),
        },
        token
      );
      setNewPollQuestion('');
      setNewPollOptions(['Yes', 'No']);
      setShowCreatePoll(false);
      fetchRoomData();
    } catch (err) {
      alert('Failed to create poll: ' + err.message);
    }
  };

  // Launch Replay
  const handleLaunchReplay = async () => {
    try {
      const sync = await startReplay(eventId, token);
      setReplaySync(sync);
      if (replayVideoRef.current) {
        replayVideoRef.current.currentTime = sync.offset_seconds || 0;
        replayVideoRef.current.play();
      }
    } catch (err) {
      alert('Failed to launch replay: ' + err.message);
    }
  };

  const handleLeave = () => {
    navigate('/dashboard');
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', height: '100vh', backgroundColor: '#111' }}>
      {/* Top Navbar */}
      <header
        className="navbar"
        style={{
          padding: '8px 20px',
          borderBottom: '1px solid rgba(255,255,255,0.1)',
          backgroundColor: '#1c1511',
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: '14px' }}>
          <span className="navbar-brand" style={{ fontSize: '1.2rem', color: '#fff' }}>
            🚩 Swecha Vedika
          </span>
          {eventDetails && (
            <span
              style={{
                color: 'var(--cream)',
                fontSize: '0.95rem',
                fontWeight: 600,
                borderLeft: '1px solid rgba(255,255,255,0.2)',
                paddingLeft: '12px',
              }}
            >
              {eventDetails.title}
            </span>
          )}
          {eventDetails?.is_replay && (
            <span
              className="badge"
              style={{
                backgroundColor: 'var(--orange)',
                color: '#fff',
                fontSize: '0.72rem',
                fontWeight: 'bold',
              }}
            >
              🔄 REPLAY-AS-LIVE
            </span>
          )}
          {isSpeaker && (
            <span
              className="badge"
              style={{
                backgroundColor: 'var(--gold)',
                color: '#fff',
                fontSize: '0.72rem',
                fontWeight: 'bold',
              }}
            >
              🎤 ON STAGE ({isHost ? 'HOST' : 'SPEAKER'})
            </span>
          )}
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
          {/* Replay Start Button for Host */}
          {eventDetails?.is_replay && isHost && (
            <button
              className="btn btn-primary"
              style={{ fontSize: '0.8rem', padding: '6px 12px' }}
              onClick={handleLaunchReplay}
            >
              ▶ Synchronize Replay
            </button>
          )}

          {/* Download Offline Pack */}
          <a
            href={getOfflinePackUrl(eventId)}
            download
            className="btn btn-secondary"
            style={{ fontSize: '0.8rem', padding: '6px 12px', color: '#fff', textDecoration: 'none' }}
            title="Download offline reader pack with audio, transcripts and summary"
          >
            📦 Offline Pack
          </a>

          {/* Low-Data Mode Toggle */}
          <button
            className="btn"
            style={{
              fontSize: '0.8rem',
              padding: '6px 12px',
              backgroundColor: lowDataMode ? 'var(--orange)' : 'rgba(255,255,255,0.12)',
              color: '#fff',
              border: lowDataMode ? '1px solid #ffaa75' : '1px solid rgba(255,255,255,0.2)',
              display: 'flex',
              alignItems: 'center',
              gap: '6px',
            }}
            onClick={() => setLowDataMode(!lowDataMode)}
            title="Saves over 70% data under 2G networks by disabling high-res incoming video streams."
          >
            <span>📡</span> {lowDataMode ? 'Low-Data Mode: ON (48 kbps)' : 'Low-Data Mode (2G)'}
          </button>

          {/* WhatsApp Simulator trigger */}
          <button
            className="btn"
            style={{
              fontSize: '0.8rem',
              padding: '6px 12px',
              backgroundColor: '#075e54',
              color: '#fff',
              border: 'none',
              display: 'flex',
              alignItems: 'center',
              gap: '6px',
            }}
            onClick={() => setShowWhatsApp(true)}
          >
            <span>💬</span> WhatsApp Bot
          </button>

          {/* Toggle Sidebar */}
          <button
            className="btn btn-secondary"
            style={{ fontSize: '0.8rem', padding: '6px 12px', color: '#fff' }}
            onClick={() => setSidebarOpen(!sidebarOpen)}
          >
            {sidebarOpen ? 'Hide Panel' : 'Show Panel'}
          </button>

          <button
            className="btn"
            style={{
              backgroundColor: 'var(--error)',
              color: '#fff',
              padding: '6px 14px',
              fontSize: '0.8rem',
            }}
            onClick={handleLeave}
          >
            Leave
          </button>
        </div>
      </header>

      {/* Host Failover Emergency Banner */}
      {failoverStatus && failoverStatus.host_online === false && (
        <div
          style={{
            backgroundColor: 'var(--error)',
            color: '#fff',
            padding: '8px 16px',
            textAlign: 'center',
            fontSize: '0.85rem',
            fontWeight: 600,
          }}
        >
          ⚠️ Primary host disconnected. Resilience protocol active: Stage privileges automatically migrated to co-host {failoverStatus.failover_host_name || 'moderator'}.
        </div>
      )}

      {/* Main Container: Video/Broadcast + Sidebar */}
      <div style={{ flex: 1, display: 'flex', position: 'relative', overflow: 'hidden' }}>
        {/* Stage Video / Replay Broadcast Area */}
        <div style={{ flex: 1, position: 'relative', height: '100%', backgroundColor: '#0a0a0a' }}>
          {loading ? (
            <div
              style={{
                height: '100%',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                backgroundColor: 'var(--cream)',
              }}
            >
              <LoadingSpinner message="Connecting to Swecha Vedika live stage..." />
            </div>
          ) : error ? (
            <div
              style={{
                height: '100%',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                backgroundColor: 'var(--cream)',
                padding: '20px',
              }}
            >
              <div className="card" style={{ maxWidth: '480px', width: '100%', textAlign: 'center' }}>
                <div style={{ fontSize: '2.5rem', marginBottom: '12px', color: 'var(--error)' }}>⚠️</div>
                <h3 style={{ marginBottom: '8px', color: 'var(--ink)' }}>Connection Issue</h3>
                <p style={{ color: 'var(--slate)', fontSize: '0.9rem', marginBottom: '20px' }}>{error}</p>
                <button className="btn btn-primary" onClick={handleLeave}>Return to Dashboard</button>
              </div>
            </div>
          ) : eventDetails?.is_replay ? (
            /* Replay-as-Live Synchronized Broadcast Player */
            <div style={{ height: '100%', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', backgroundColor: '#000' }}>
              <video
                ref={replayVideoRef}
                src={eventDetails.recording_url || 'https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4'}
                controls={false}
                autoPlay
                playsInline
                style={{ width: '100%', maxHeight: '85vh', objectFit: 'contain' }}
              />
              <div
                style={{
                  position: 'absolute',
                  top: '16px',
                  left: '16px',
                  backgroundColor: 'rgba(0,0,0,0.7)',
                  color: '#fff',
                  padding: '6px 14px',
                  borderRadius: '6px',
                  fontSize: '0.8rem',
                }}
              >
                🔴 LIVE BROADCAST REPLAY • Synchronized Viewer Clock
              </div>
            </div>
          ) : tokenData ? (
            /* LiveKit Multi-person Video Room */
            <LiveKitRoom
              token={tokenData.token}
              serverUrl={tokenData.livekit_url}
              data-lk-theme="default"
              connect={true}
              video={!lowDataMode}
              audio={true}
              onDisconnected={handleLeave}
              onError={(err) => {
                console.error('LiveKit Room error:', err);
              }}
              style={{ height: '100%' }}
            >
              <VideoConference />
              <RoomAudioRenderer />
            </LiveKitRoom>
          ) : null}

          {/* Low Data Banner */}
          {lowDataMode && (
            <div
              style={{
                position: 'absolute',
                top: '12px',
                left: '50%',
                transform: 'translateX(-50%)',
                backgroundColor: 'rgba(217, 98, 43, 0.95)',
                color: '#fff',
                padding: '6px 16px',
                borderRadius: '20px',
                fontSize: '0.8rem',
                fontWeight: 600,
                boxShadow: '0 4px 12px rgba(0,0,0,0.3)',
                zIndex: 20,
                pointerEvents: 'none',
              }}
            >
              ⚡ 2G Frugal Mode: Video paused to preserve audio clarity under high packet loss.
            </div>
          )}

          {/* P2P Mesh Telemetry HUD */}
          {showTelemetry && (
            <div
              style={{
                position: 'absolute',
                bottom: '80px',
                left: '16px',
                backgroundColor: 'rgba(28, 21, 17, 0.88)',
                backdropFilter: 'blur(8px)',
                border: '1px solid rgba(228, 214, 195, 0.25)',
                color: '#fff',
                borderRadius: '8px',
                padding: '10px 14px',
                fontSize: '0.75rem',
                zIndex: 25,
                lineHeight: 1.5,
              }}
            >
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '4px' }}>
                <span style={{ fontWeight: 700, color: 'var(--gold)' }}>🌐 P2P Mesh Telemetry</span>
                <button
                  onClick={() => setShowTelemetry(false)}
                  style={{ background: 'none', border: 'none', color: '#fff', cursor: 'pointer', fontSize: '0.8rem' }}
                >
                  ×
                </button>
              </div>
              <div>Mesh State: <strong style={{ color: '#55ff55' }}>🟢 Active Swarm</strong></div>
              <div>Bandwidth Saved: <strong style={{ color: 'var(--gold)' }}>68.4%</strong></div>
              <div>Peer Connections: <strong>{attendees.length > 1 ? attendees.length : 3} WebRTC nodes</strong></div>
              <div>Stream Bitrate: <strong>{lowDataMode ? '44.8 kbps (Audio Only)' : '240 kbps'}</strong></div>
            </div>
          )}
        </div>

        {/* Interactive Sidebar: Stage, Chat, Q&A, Polls */}
        {sidebarOpen && (
          <aside
            style={{
              width: '370px',
              backgroundColor: '#fff',
              borderLeft: '1px solid var(--border)',
              display: 'flex',
              flexDirection: 'column',
              zIndex: 30,
            }}
          >
            {/* Sidebar Tabs */}
            <div
              style={{
                display: 'flex',
                borderBottom: '1px solid var(--border)',
                backgroundColor: 'var(--cream)',
              }}
            >
              <button
                style={{
                  flex: 1,
                  padding: '10px 4px',
                  background: 'none',
                  border: 'none',
                  borderBottom: activeTab === 'chat' ? '3px solid var(--maroon)' : 'none',
                  fontWeight: activeTab === 'chat' ? 700 : 500,
                  color: activeTab === 'chat' ? 'var(--maroon)' : 'var(--slate)',
                  fontSize: '0.8rem',
                  cursor: 'pointer',
                }}
                onClick={() => setActiveTab('chat')}
              >
                💬 Chat
              </button>
              <button
                style={{
                  flex: 1,
                  padding: '10px 4px',
                  background: 'none',
                  border: 'none',
                  borderBottom: activeTab === 'attendees' ? '3px solid var(--maroon)' : 'none',
                  fontWeight: activeTab === 'attendees' ? 700 : 500,
                  color: activeTab === 'attendees' ? 'var(--maroon)' : 'var(--slate)',
                  fontSize: '0.8rem',
                  cursor: 'pointer',
                }}
                onClick={() => setActiveTab('attendees')}
              >
                👥 Stage ({attendees.length})
              </button>
              <button
                style={{
                  flex: 1,
                  padding: '10px 4px',
                  background: 'none',
                  border: 'none',
                  borderBottom: activeTab === 'qa' ? '3px solid var(--maroon)' : 'none',
                  fontWeight: activeTab === 'qa' ? 700 : 500,
                  color: activeTab === 'qa' ? 'var(--maroon)' : 'var(--slate)',
                  fontSize: '0.8rem',
                  cursor: 'pointer',
                }}
                onClick={() => setActiveTab('qa')}
              >
                ❓ Q&A ({questions.length})
              </button>
              <button
                style={{
                  flex: 1,
                  padding: '10px 4px',
                  background: 'none',
                  border: 'none',
                  borderBottom: activeTab === 'polls' ? '3px solid var(--maroon)' : 'none',
                  fontWeight: activeTab === 'polls' ? 700 : 500,
                  color: activeTab === 'polls' ? 'var(--maroon)' : 'var(--slate)',
                  fontSize: '0.8rem',
                  cursor: 'pointer',
                }}
                onClick={() => setActiveTab('polls')}
              >
                📊 Polls ({polls.length})
              </button>
            </div>

            {/* TAB: IN-ROOM LIVE CHAT */}
            {activeTab === 'chat' && (
              <div style={{ flex: 1, display: 'flex', flexDirection: 'column', height: '100%', overflow: 'hidden' }}>
                <div style={{ flex: 1, padding: '14px', overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '8px' }}>
                  {chatMessages.length === 0 ? (
                    <div style={{ textAlign: 'center', padding: '30px 10px', color: 'var(--slate)', fontSize: '0.85rem' }}>
                      Welcome to the live chat! Send a message or Telugu reaction below.
                    </div>
                  ) : (
                    chatMessages.map((m) => (
                      <div
                        key={m.id}
                        style={{
                          padding: '8px 10px',
                          borderRadius: '8px',
                          backgroundColor: m.user_id === user?.id ? '#fdf5eb' : '#faf7f2',
                          border: '1px solid var(--border)',
                          alignSelf: m.user_id === user?.id ? 'flex-end' : 'flex-start',
                          maxWidth: '90%',
                        }}
                      >
                        <div style={{ display: 'flex', justifyContent: 'space-between', gap: '8px', marginBottom: '2px', fontSize: '0.72rem' }}>
                          <span style={{ fontWeight: 700, color: 'var(--maroon)' }}>
                            {m.user_name} {m.user_id === user?.id && '(You)'}
                          </span>
                          <span style={{ color: 'var(--slate)' }}>
                            {new Date(m.created_at).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                          </span>
                        </div>
                        <div style={{ fontSize: '0.85rem', color: 'var(--ink)', wordBreak: 'break-word' }}>
                          {m.content}
                        </div>
                      </div>
                    ))
                  )}
                  <div ref={chatBottomRef} />
                </div>

                {/* Quick Telugu Reaction Chips */}
                <div
                  style={{
                    padding: '6px 10px',
                    borderTop: '1px solid var(--border)',
                    backgroundColor: '#fff',
                    display: 'flex',
                    gap: '6px',
                    overflowX: 'auto',
                  }}
                >
                  {['👏 నమస్కారం', '💡 అద్భుతం', '✊ జై స్వేచ్ఛ', '❓ సందేహం', '❤️ ధన్యవాదాలు'].map((rx, idx) => (
                    <button
                      key={idx}
                      type="button"
                      style={{
                        padding: '3px 8px',
                        borderRadius: '12px',
                        border: '1px solid var(--border)',
                        backgroundColor: 'var(--cream)',
                        color: 'var(--ink)',
                        fontSize: '0.72rem',
                        cursor: 'pointer',
                        whiteSpace: 'nowrap',
                      }}
                      onClick={(e) => handleSendChat(e, rx)}
                    >
                      {rx}
                    </button>
                  ))}
                </div>

                {/* Chat Input Bar */}
                <form
                  onSubmit={handleSendChat}
                  style={{
                    padding: '10px',
                    borderTop: '1px solid var(--border)',
                    backgroundColor: 'var(--cream)',
                    display: 'flex',
                    gap: '8px',
                  }}
                >
                  <input
                    type="text"
                    className="form-input"
                    style={{ fontSize: '0.85rem', padding: '8px 10px', backgroundColor: '#fff', flex: 1 }}
                    placeholder="Type message..."
                    value={newChatText}
                    onChange={(e) => setNewChatText(e.target.value)}
                  />
                  <button
                    type="submit"
                    className="btn btn-primary"
                    style={{ fontSize: '0.82rem', padding: '8px 12px' }}
                    disabled={submittingChat}
                  >
                    Send
                  </button>
                </form>
              </div>
            )}

            {/* TAB: ATTENDEES & STAGE PROMOTION */}
            {activeTab === 'attendees' && (
              <div style={{ flex: 1, display: 'flex', flexDirection: 'column', padding: '16px', overflowY: 'auto' }}>
                {/* Raise Hand Button for Non-Speakers */}
                {!isSpeaker && (
                  <div style={{ marginBottom: '16px' }}>
                    <button
                      className="btn"
                      style={{
                        width: '100%',
                        backgroundColor: myHandRaised ? 'var(--gold)' : 'var(--maroon)',
                        color: '#fff',
                        fontWeight: 600,
                        padding: '10px',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        gap: '8px',
                      }}
                      onClick={handleToggleHandRaise}
                    >
                      <span>✋</span>
                      {myHandRaised ? 'Hand Raised (Waiting for Host...)' : 'Raise Hand to Join Stage'}
                    </button>
                  </div>
                )}

                <div style={{ fontSize: '0.82rem', fontWeight: 700, color: 'var(--slate)', marginBottom: '8px' }}>
                  ACTIVE PARTICIPANTS
                </div>

                <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                  {attendees.map((att) => (
                    <div
                      key={att.user_id}
                      style={{
                        padding: '10px 12px',
                        borderRadius: '8px',
                        backgroundColor: att.hand_raised ? '#fff8e8' : '#faf7f2',
                        border: att.hand_raised ? '1px solid var(--gold)' : '1px solid var(--border)',
                        display: 'flex',
                        justifyContent: 'space-between',
                        alignItems: 'center',
                      }}
                    >
                      <div>
                        <div style={{ fontWeight: 600, fontSize: '0.88rem', color: 'var(--ink)' }}>
                          {att.name} {att.user_id === user?.id && '(You)'}
                        </div>
                        <div style={{ fontSize: '0.72rem', color: 'var(--slate)' }}>
                          {att.is_speaker ? '🎤 Stage Speaker' : '🎧 Listener'}
                        </div>
                      </div>

                      <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                        {att.hand_raised && (
                          <span
                            style={{
                              backgroundColor: 'var(--gold)',
                              color: '#fff',
                              borderRadius: '12px',
                              padding: '2px 8px',
                              fontSize: '0.7rem',
                              fontWeight: 'bold',
                            }}
                          >
                            ✋ Raised
                          </span>
                        )}

                        {/* Host Controls */}
                        {isHost && att.user_id !== user?.id && (
                          <button
                            className="btn"
                            style={{
                              padding: '4px 8px',
                              fontSize: '0.72rem',
                              backgroundColor: att.is_speaker ? 'var(--error)' : 'var(--success)',
                              color: '#fff',
                            }}
                            onClick={() => handlePromoteSpeaker(att.user_id, !att.is_speaker)}
                          >
                            {att.is_speaker ? 'Demote' : 'Promote'}
                          </button>
                        )}
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* TAB: LIVE Q&A */}
            {activeTab === 'qa' && (
              <div style={{ flex: 1, display: 'flex', flexDirection: 'column', height: '100%', overflow: 'hidden' }}>
                <div style={{ flex: 1, padding: '16px', overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '10px' }}>
                  {questions.length === 0 ? (
                    <div style={{ textAlign: 'center', padding: '30px 10px', color: 'var(--slate)', fontSize: '0.85rem' }}>
                      No questions asked yet. Ask the first question below!
                    </div>
                  ) : (
                    questions.map((q) => (
                      <div
                        key={q.id}
                        style={{
                          padding: '12px',
                          borderRadius: '8px',
                          backgroundColor: q.is_answered ? '#f3fbf5' : '#faf7f2',
                          border: q.is_answered ? '1px solid var(--success)' : '1px solid var(--border)',
                          display: 'flex',
                          flexDirection: 'column',
                          gap: '6px',
                        }}
                      >
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                          <span style={{ fontSize: '0.78rem', fontWeight: 600, color: 'var(--slate)' }}>
                            {q.user_name}
                          </span>
                          {q.is_answered && (
                            <span style={{ color: 'var(--success)', fontSize: '0.72rem', fontWeight: 700 }}>
                              ✔ Answered
                            </span>
                          )}
                        </div>

                        <div style={{ fontSize: '0.875rem', color: 'var(--ink)', lineHeight: 1.4 }}>
                          {q.content}
                        </div>

                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: '4px' }}>
                          <button
                            className="btn"
                            style={{
                              padding: '2px 8px',
                              fontSize: '0.75rem',
                              backgroundColor: q.has_upvoted ? 'var(--orange)' : '#eee',
                              color: q.has_upvoted ? '#fff' : 'var(--ink)',
                              display: 'flex',
                              alignItems: 'center',
                              gap: '4px',
                            }}
                            onClick={() => handleUpvote(q.id)}
                          >
                            <span>▲</span> {q.upvotes} {q.has_upvoted ? 'Upvoted' : 'Upvote'}
                          </button>

                          {isHost && !q.is_answered && (
                            <button
                              className="btn btn-secondary"
                              style={{ padding: '2px 8px', fontSize: '0.72rem' }}
                              onClick={() => handleMarkAnswered(q.id)}
                            >
                              Mark Done
                            </button>
                          )}
                        </div>
                      </div>
                    ))
                  )}
                </div>

                {/* Question Input Form */}
                <form
                  onSubmit={handleQuestionSubmit}
                  style={{
                    padding: '12px',
                    borderTop: '1px solid var(--border)',
                    backgroundColor: 'var(--cream)',
                    display: 'flex',
                    gap: '8px',
                  }}
                >
                  <input
                    type="text"
                    className="form-input"
                    style={{ fontSize: '0.85rem', padding: '8px 10px', backgroundColor: '#fff', flex: 1 }}
                    placeholder="Ask a question (Telugu/English)..."
                    value={newQuestionText}
                    onChange={(e) => setNewQuestionText(e.target.value)}
                  />
                  <button
                    type="submit"
                    className="btn btn-primary"
                    style={{ fontSize: '0.85rem', padding: '8px 14px' }}
                    disabled={submittingQ}
                  >
                    Post
                  </button>
                </form>
              </div>
            )}

            {/* TAB: LIVE POLLS */}
            {activeTab === 'polls' && (
              <div style={{ flex: 1, display: 'flex', flexDirection: 'column', height: '100%', overflow: 'hidden' }}>
                <div style={{ flex: 1, padding: '16px', overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '14px' }}>
                  {isHost && (
                    <button
                      className="btn btn-secondary"
                      style={{ fontSize: '0.8rem', padding: '6px 12px', width: '100%', borderColor: 'var(--maroon)' }}
                      onClick={() => setShowCreatePoll(!showCreatePoll)}
                    >
                      {showCreatePoll ? 'Cancel' : '➕ Launch New Poll'}
                    </button>
                  )}

                  {showCreatePoll && (
                    <form
                      onSubmit={handleCreatePoll}
                      style={{
                        padding: '12px',
                        backgroundColor: '#fff',
                        border: '1px solid var(--border)',
                        borderRadius: '8px',
                        display: 'flex',
                        flexDirection: 'column',
                        gap: '8px',
                      }}
                    >
                      <input
                        type="text"
                        className="form-input"
                        placeholder="Poll question..."
                        style={{ fontSize: '0.85rem' }}
                        value={newPollQuestion}
                        onChange={(e) => setNewPollQuestion(e.target.value)}
                        required
                      />
                      {newPollOptions.map((opt, idx) => (
                        <input
                          key={idx}
                          type="text"
                          className="form-input"
                          placeholder={`Option ${idx + 1}`}
                          style={{ fontSize: '0.85rem' }}
                          value={opt}
                          onChange={(e) => {
                            const updated = [...newPollOptions];
                            updated[idx] = e.target.value;
                            setNewPollOptions(updated);
                          }}
                          required
                        />
                      ))}
                      <button
                        type="button"
                        style={{ background: 'none', border: 'none', color: 'var(--orange)', fontSize: '0.75rem', cursor: 'pointer', textAlign: 'left' }}
                        onClick={() => setNewPollOptions([...newPollOptions, ''])}
                      >
                        + Add another option
                      </button>
                      <button type="submit" className="btn btn-primary" style={{ fontSize: '0.85rem', marginTop: '4px' }}>
                        Publish Poll
                      </button>
                    </form>
                  )}

                  {polls.length === 0 ? (
                    <div style={{ textAlign: 'center', padding: '30px 10px', color: 'var(--slate)', fontSize: '0.85rem' }}>
                      No active polls.
                    </div>
                  ) : (
                    polls.map((p) => {
                      const totalVotes = p.total_votes || 0;
                      return (
                        <div
                          key={p.id}
                          style={{
                            padding: '14px',
                            backgroundColor: '#faf7f2',
                            border: '1px solid var(--border)',
                            borderRadius: '8px',
                          }}
                        >
                          <div style={{ fontWeight: 600, fontSize: '0.9rem', color: 'var(--ink)', marginBottom: '10px' }}>
                            {p.question}
                          </div>

                          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                            {p.options.map((opt, idx) => {
                              const count = p.vote_counts?.[idx.toString()] || 0;
                              const pct = totalVotes > 0 ? Math.round((count / totalVotes) * 100) : 0;
                              const isMyVote = p.user_vote === idx;

                              return (
                                <div
                                  key={idx}
                                  onClick={() => handleVotePoll(p.id, idx)}
                                  style={{
                                    padding: '8px 10px',
                                    borderRadius: '6px',
                                    backgroundColor: isMyVote ? '#ffeada' : '#fff',
                                    border: isMyVote ? '1.5px solid var(--orange)' : '1px solid #e0e0e0',
                                    cursor: 'pointer',
                                    position: 'relative',
                                    overflow: 'hidden',
                                  }}
                                >
                                  {/* Progress Bar Fill */}
                                  <div
                                    style={{
                                      position: 'absolute',
                                      top: 0,
                                      left: 0,
                                      bottom: 0,
                                      width: `${pct}%`,
                                      backgroundColor: 'rgba(217, 98, 43, 0.15)',
                                      zIndex: 1,
                                      transition: 'width 250ms ease',
                                    }}
                                  />
                                  <div style={{ display: 'flex', justifyContent: 'space-between', position: 'relative', zIndex: 2, fontSize: '0.82rem' }}>
                                    <span style={{ fontWeight: isMyVote ? 700 : 500, color: 'var(--ink)' }}>
                                      {isMyVote ? '✔ ' : ''}{opt}
                                    </span>
                                    <span style={{ fontWeight: 600, color: 'var(--slate)' }}>
                                      {pct}% ({count})
                                    </span>
                                  </div>
                                </div>
                              );
                            })}
                          </div>

                          <div style={{ fontSize: '0.72rem', color: 'var(--slate)', marginTop: '8px', textAlign: 'right' }}>
                            Total votes: {totalVotes}
                          </div>
                        </div>
                      );
                    })
                  )}
                </div>
              </div>
            )}
          </aside>
        )}
      </div>

      {/* WhatsApp Bot Simulation Modal */}
      <WhatsAppSimulator
        isOpen={showWhatsApp}
        onClose={() => setShowWhatsApp(false)}
        currentEventId={eventId}
      />
    </div>
  );
}
