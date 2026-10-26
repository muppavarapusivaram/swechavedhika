import { useState } from 'react';
import { Link } from 'react-router-dom';

export default function EventCard({ event, onJoin, isJoined = false }) {
  const [joining, setJoining] = useState(false);
  const [joined, setJoined] = useState(isJoined);

  const handleJoin = async () => {
    if (joining) return;
    setJoining(true);
    try {
      await onJoin(event.id);
      setJoined(true);
    } catch {
      // Error handled in parent notification if needed
    } finally {
      setJoining(false);
    }
  };

  const formatDate = (dateString) => {
    if (!dateString) return 'Date TBA';
    try {
      const date = new Date(dateString);
      return new Intl.DateTimeFormat('en-US', {
        month: 'short',
        day: 'numeric',
        year: 'numeric',
        hour: 'numeric',
        minute: '2-digit',
        hour12: true,
      }).format(date);
    } catch {
      return dateString;
    }
  };

  const statusClass =
    event.status === 'live'
      ? 'badge-live'
      : event.status === 'ended'
      ? 'badge-ended'
      : 'badge-scheduled';

  return (
    <div className="card event-card">
      <div>
        <div className="event-card-header">
          <h3 className="event-title">{event.title}</h3>
          <span className={`badge ${statusClass}`}>{event.status}</span>
        </div>

        <p className="event-desc">
          {event.description || 'No description provided.'}
        </p>
      </div>

      <div className="event-meta">
        <span className="event-time">
          🕒 {formatDate(event.scheduled_start)}
        </span>

        <div style={{ display: 'flex', gap: '8px', alignItems: 'center', flexWrap: 'wrap' }}>
          <button
            className={`btn ${joined ? 'btn-joined' : 'btn-join'}`}
            onClick={handleJoin}
            disabled={joining}
          >
            {joining ? (
              'Joining...'
            ) : joined ? (
              <>
                <span>✓</span> Joined
              </>
            ) : (
              'Join Event'
            )}
          </button>

          {joined && (
            <Link
              to={`/room/${event.id}`}
              className="btn btn-primary"
              style={{ padding: '8px 14px', fontSize: '0.875rem' }}
            >
              Enter Room →
            </Link>
          )}
        </div>
      </div>
    </div>
  );
}
