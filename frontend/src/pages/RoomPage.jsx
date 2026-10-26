import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import '@livekit/components-styles';
import {
  LiveKitRoom,
  VideoConference,
  RoomAudioRenderer,
} from '@livekit/components-react';
import LoadingSpinner from '../components/LoadingSpinner';
import { useAuth } from '../context/AuthContext';

export default function RoomPage() {
  const { eventId } = useParams();
  const navigate = useNavigate();
  const { authFetch, user } = useAuth();

  const [tokenData, setTokenData] = useState(null);
  const [eventDetails, setEventDetails] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let isMounted = true;

    async function initRoom() {
      setLoading(true);
      setError(null);
      try {
        // Fetch event info for header display
        const event = await authFetch(`/events/${eventId}`);
        if (!isMounted) return;
        setEventDetails(event);

        // Fetch LiveKit room token
        const tokenRes = await authFetch(`/events/${eventId}/token`, {
          method: 'POST',
        });
        if (!isMounted) return;
        setTokenData(tokenRes);
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

  const handleLeave = () => {
    navigate('/dashboard');
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', height: '100vh', backgroundColor: '#111' }}>
      {/* Room Header */}
      <header
        className="navbar"
        style={{
          padding: '10px 20px',
          borderBottom: '1px solid rgba(255,255,255,0.1)',
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: '14px' }}>
          <span className="navbar-brand" style={{ fontSize: '1.2rem' }}>
            Swecha Vedika
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
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          {user && (
            <span style={{ color: 'rgba(255,255,255,0.8)', fontSize: '0.85rem' }}>
              Logged in as <strong style={{ color: '#fff' }}>{user.name}</strong>
            </span>
          )}
          <button
            className="btn"
            style={{
              backgroundColor: 'var(--error)',
              color: '#fff',
              padding: '6px 14px',
              fontSize: '0.85rem',
            }}
            onClick={handleLeave}
          >
            Leave Room
          </button>
        </div>
      </header>

      {/* Main Video Call Area */}
      <main style={{ flex: 1, position: 'relative', overflow: 'hidden' }}>
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
            <LoadingSpinner message="Initializing LiveKit video room..." />
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
              <div style={{ fontSize: '2.5rem', marginBottom: '12px', color: 'var(--error)' }}>
                ⚠️
              </div>
              <h3 style={{ marginBottom: '8px', color: 'var(--ink)' }}>
                Connection Issue
              </h3>
              <p style={{ color: 'var(--slate)', fontSize: '0.9rem', marginBottom: '20px' }}>
                {error}
              </p>
              <button className="btn btn-primary" onClick={handleLeave}>
                Return to Dashboard
              </button>
            </div>
          </div>
        ) : tokenData ? (
          <LiveKitRoom
            token={tokenData.token}
            serverUrl={tokenData.livekit_url}
            data-lk-theme="default"
            connect={true}
            video={true}
            audio={true}
            onDisconnected={handleLeave}
            onError={(err) => {
              console.error('LiveKit Room error:', err);
              setError(`LiveKit connection error: ${err.message}`);
            }}
            style={{ height: '100%' }}
          >
            <VideoConference />
            <RoomAudioRenderer />
          </LiveKitRoom>
        ) : null}
      </main>
    </div>
  );
}
