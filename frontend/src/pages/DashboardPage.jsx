import { useState, useEffect, useCallback } from 'react';
import Navbar from '../components/Navbar';
import CreateEventForm from '../components/CreateEventForm';
import EventCard from '../components/EventCard';
import LoadingSpinner from '../components/LoadingSpinner';
import { useAuth } from '../context/AuthContext';

export default function DashboardPage() {
  const { authFetch } = useAuth();
  const [events, setEvents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [joinedEventIds, setJoinedEventIds] = useState(new Set());
  const [feedback, setFeedback] = useState(null);

  const fetchEvents = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await authFetch('/events');
      setEvents(data);
    } catch (err) {
      if (err.status !== 401) {
        setError(err.message || 'Failed to load events.');
      }
    } finally {
      setLoading(false);
    }
  }, [authFetch]);

  useEffect(() => {
    fetchEvents();
  }, [fetchEvents]);

  const handleCreateEvent = async (eventPayload) => {
    const created = await authFetch('/events', {
      method: 'POST',
      data: eventPayload,
    });
    setEvents((prev) => [created, ...prev]);
    setFeedback({
      type: 'success',
      message: `Event "${created.title}" published successfully!`,
    });
    setTimeout(() => setFeedback(null), 4000);
  };

  const handleJoinEvent = async (eventId) => {
    await authFetch(`/events/${eventId}/join`, {
      method: 'POST',
    });
    setJoinedEventIds((prev) => new Set([...prev, eventId]));
  };

  return (
    <div className="app-container">
      <Navbar />

      <main className="main-content">
        <div className="page-header">
          <div>
            <h2 className="page-title">Community Broadcasts</h2>
            <p style={{ color: 'var(--slate)', fontSize: '0.95rem' }}>
              Browse scheduled sessions or schedule a new broadcast
            </p>
          </div>
        </div>

        {feedback && (
          <div className={`alert alert-${feedback.type}`}>{feedback.message}</div>
        )}

        <CreateEventForm onEventCreated={handleCreateEvent} />

        <div style={{ marginTop: '28px' }}>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '16px' }}>
            <h3 style={{ fontSize: '1.25rem', fontWeight: 700, color: 'var(--ink)' }}>
              Upcoming Sessions {events.length > 0 && `(${events.length})`}
            </h3>

            <button
              type="button"
              className="btn btn-secondary"
              style={{ fontSize: '0.85rem', padding: '6px 14px' }}
              onClick={fetchEvents}
              disabled={loading}
            >
              ↻ Refresh
            </button>
          </div>

          {loading ? (
            <LoadingSpinner message="Fetching upcoming events..." />
          ) : error ? (
            <div className="alert alert-error">
              <span>{error}</span>
              <button
                className="btn btn-secondary"
                style={{ marginLeft: 'auto', padding: '4px 10px', fontSize: '0.8rem' }}
                onClick={fetchEvents}
              >
                Retry
              </button>
            </div>
          ) : events.length === 0 ? (
            <div className="empty-state">
              <div className="empty-icon">📅</div>
              <h4 className="empty-title">No events scheduled yet</h4>
              <p className="empty-desc">
                Be the first to create a broadcast! Click "+ Create Event" above to
                schedule your session.
              </p>
            </div>
          ) : (
            <div className="events-grid">
              {events.map((event) => (
                <EventCard
                  key={event.id}
                  event={event}
                  onJoin={handleJoinEvent}
                  isJoined={joinedEventIds.has(event.id)}
                />
              ))}
            </div>
          )}
        </div>
      </main>
    </div>
  );
}
