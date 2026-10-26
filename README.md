# Swecha Vedika

A self-hosted meeting and broadcast platform prototype designed for community civic-tech events, interactive meetings, and scalable real-time communication.

> **Status**: **Step 5 (LiveKit Video Rooms)** is active. Local multi-person WebRTC video calling powered by self-hosted LiveKit Server is integrated with FastAPI token generation and the Swecha Vedika React frontend.

---

## Services & Ports

| Service | Technology | Internal Port | Host Port | External URL |
| :--- | :--- | :--- | :--- | :--- |
| **Frontend** | React 18 + Vite | 5173 | 5173 | [http://localhost:5173](http://localhost:5173) |
| **Backend** | FastAPI + Python 3.11 | 8000 | 8000 | [http://localhost:8000](http://localhost:8000) |
| **Database** | PostgreSQL 16 | 5432 | 5432 | `localhost:5432` |
| **LiveKit Server** | LiveKit (Go/WebRTC) | 7880, 7881, 7882 | 7880, 7881, 7882/udp | `ws://localhost:7880` |

---

## Video Rooms

Video rooms in Swecha Vedika are powered by **LiveKit Server** running locally inside Docker:
- **No External Account Needed**: LiveKit runs 100% locally in development mode without LiveKit Cloud or third-party dependencies.
- **Room Mapping**: Each event's unique UUID (`event.id`) serves as the LiveKit room name. All attendees who join that event and enter the room are connected to the same live video session.
- **Token Generation**: When a user navigates to `/room/:eventId`, the backend verifies authentication and event existence, then generates a signed LiveKit JWT granting room join, publishing, and subscribing permissions scoped to their user identity and display name.
- **Media Architecture**:
  - `7880 TCP`: Signaling WebSocket and HTTP management API.
  - `7881 TCP`: WebRTC ICE over TCP fallback.
  - `7882 UDP`: Direct WebRTC media transmission.

---

## Frontend Pages

The frontend application runs on `http://localhost:5173` with client-side routing via `react-router-dom`:

| Route | Access | Description |
| :--- | :---: | :--- |
| `/` | Public | Root redirector: redirects to `/dashboard` if logged in, otherwise redirects to `/login`. |
| `/login` | Public | Branded sign-in card with email and password fields, inline validation, and error banner for invalid credentials (HTTP 401). |
| `/register` | Public | Branded registration card (name, email, phone number, password) with client-side validation and duplicate-email error handling (HTTP 400). Automatically logs in on creation. |
| `/dashboard` | **Protected** | Authenticated community dashboard featuring: <br>• Sticky maroon header with brand name, user role pill, and logout button.<br>• Expandable event creation card with datetime-local picker.<br>• Responsive grid of event cards with status badges (`scheduled`, `live`, `ended`).<br>• One-click **Join Event** button with an interactive confirmation pulse (`✓ Joined`).<br>• **Enter Room** button linking directly to `/room/:eventId`.<br>• Tasteful loading and empty states. |
| `/room/:eventId` | **Protected** | Full-screen interactive video conference room powered by `@livekit/components-react`: <br>• Automatic LiveKit token acquisition for the selected event.<br>• Video/audio tile grid for all active participants.<br>• Camera, microphone, and device toggle controls.<br>• **Leave Room** button returning gracefully to `/dashboard`. |

> **Security Note**: JWT authentication tokens are stored strictly **in memory** (React state / `AuthContext`) and are never written to `localStorage` or `sessionStorage`. Refreshing the browser will intentionally require re-logging in.

---

## Design System

The application styling follows a dedicated warm, civic-tech color palette configured as CSS custom properties in [frontend/src/index.css](frontend/src/index.css):

```css
:root {
  --maroon: #7A1F1A;       /* Primary brand color (headers, primary buttons) */
  --maroon-dark: #5C1712;  /* Hover states for primary elements */
  --orange: #D9622B;       /* Accent color (links, secondary buttons, highlights) */
  --gold: #C9962F;         /* Badges, active states, borders */
  --cream: #FBF5EA;        /* Page background */
  --white: #FFFFFF;        /* Card backgrounds */
  --ink: #2B211A;          /* Primary text */
  --slate: #5C4C3E;        /* Secondary/muted text */
  --border: #E4D6C3;       /* Card borders, dividers */
  --success: #2E6B3E;      /* Join confirmations, live badges */
  --error: #B3261E;        /* Error banners, invalid field borders */
}
```

---

## Database Schema

The database consists of three core tables managed via SQLAlchemy models and Alembic migrations:

### 1. `users`
- `id` (UUID, Primary Key, auto-generated)
- `name` (String(255), required)
- `email` (String(255), required, unique, indexed)
- `phone_number` (String(50), required)
- `password_hash` (String(255), required, hashed with bcrypt)
- `role` (Enum `user_role`: `'owner'`, `'host'`, `'moderator'`, `'speaker'`, `'viewer'`; default: `'viewer'`)
- `created_at` (Timestamp with timezone, default: `now()`)

### 2. `events`
- `id` (UUID, Primary Key, auto-generated)
- `title` (String(255), required)
- `description` (Text, optional)
- `host_id` (UUID, Foreign Key referencing `users.id` with `ON DELETE CASCADE`, required, indexed)
- `scheduled_start` (Timestamp with timezone, required)
- `status` (Enum `event_status`: `'scheduled'`, `'live'`, `'ended'`; default: `'scheduled'`)
- `created_at` (Timestamp with timezone, default: `now()`)

### 3. `attendance`
- `id` (UUID, Primary Key, auto-generated)
- `event_id` (UUID, Foreign Key referencing `events.id` with `ON DELETE CASCADE`, required, indexed)
- `user_id` (UUID, Foreign Key referencing `users.id` with `ON DELETE CASCADE`, required, indexed)
- `joined_at` (Timestamp with timezone, default: `now()`)
- `left_at` (Timestamp with timezone, nullable)

---

## API Endpoints

Interactive Swagger UI documentation is available at [http://localhost:8000/docs](http://localhost:8000/docs).

| Method | Path | Auth Required | Description |
| :--- | :--- | :---: | :--- |
| `GET` | `/health` | No | Basic health check returning `{"status": "ok"}` |
| `GET` | `/health/db` | No | Verifies DB connection and returns table row counts |
| `POST` | `/auth/register` | No | Registers a new user (`viewer` role), hashes password with bcrypt, and returns a JWT access token |
| `POST` | `/auth/login` | No | Authenticates user credentials and returns a JWT access token |
| `GET` | `/auth/me` | **Bearer JWT** | Returns profile information for the authenticated user |
| `GET` | `/events` | **Bearer JWT** | Returns list of all scheduled events ordered by `scheduled_start` |
| `POST` | `/events` | **Bearer JWT** | Creates a new event hosted by the currently authenticated user |
| `GET` | `/events/{event_id}` | **Bearer JWT** | Retrieves details for a specific event by UUID |
| `POST` | `/events/{event_id}/join` | **Bearer JWT** | Records attendance for the authenticated user (idempotent) |
| `POST` | `/events/{event_id}/token` | **Bearer JWT** | Generates a signed LiveKit WebRTC access token for the event room |

---

## Getting Started

### 1. Configure Environment Variables
Copy the example environment configuration file to `.env`:

```bash
cp .env.example .env
```
*(On Windows Command Prompt / PowerShell: `copy .env.example .env`)*

### 2. Start All Services
Build images and run all four containers (`db`, `livekit`, `backend`, `frontend`):

```bash
docker compose up --build
```

To run in the background (detached mode):
```bash
docker compose up --build -d
```

### 3. Open in Browser
Open your browser and navigate to:
**[http://localhost:5173](http://localhost:5173)**

---

## Stopping the Services
To stop running containers:
```bash
docker compose down
```

To stop containers and wipe persistent database volume:
```bash
docker compose down -v
```
