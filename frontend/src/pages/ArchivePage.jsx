import { useState, useEffect, useRef } from 'react';
import Navbar from '../components/Navbar';
import LoadingSpinner from '../components/LoadingSpinner';
import { searchArchive, getCorpus, populateDemoAi, getOfflinePackUrl } from '../api/client';
import { useAuth } from '../context/AuthContext';

export default function ArchivePage() {
  const { token, user } = useAuth();
  const [events, setEvents] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedLanguage, setSelectedLanguage] = useState('All');
  const [selectedEvent, setSelectedEvent] = useState(null);
  const [loading, setLoading] = useState(true);
  const [actionLoading, setActionLoading] = useState(false);
  const [error, setError] = useState(null);
  const [currentTime, setCurrentTime] = useState(0);

  const videoRef = useRef(null);

  const fetchArchive = async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await searchArchive(searchQuery, selectedLanguage === 'All' ? '' : selectedLanguage);
      setEvents(data);
      if (data.length > 0 && !selectedEvent) {
        setSelectedEvent(data[0]);
      } else if (selectedEvent) {
        const updated = data.find((e) => e.id === selectedEvent.id);
        if (updated) setSelectedEvent(updated);
      }
    } catch (err) {
      setError(err.message || 'Failed to load archive');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    const timer = setTimeout(() => {
      fetchArchive();
    }, 300);
    return () => clearTimeout(timer);
  }, [searchQuery, selectedLanguage]);

  const handleExportCorpus = async () => {
    try {
      const corpus = await getCorpus();
      const blob = new Blob([JSON.stringify(corpus, null, 2)], {
        type: 'application/json',
      });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `swecha_telugu_speech_corpus_${new Date().toISOString().slice(0, 10)}.json`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    } catch (err) {
      alert('Failed to export corpus: ' + err.message);
    }
  };

  const handlePopulateDemo = async (eventId) => {
    if (!token) return;
    setActionLoading(true);
    try {
      const updated = await populateDemoAi(eventId, token);
      setSelectedEvent(updated);
      fetchArchive();
    } catch (err) {
      alert('Failed to populate AI data: ' + err.message);
    } finally {
      setActionLoading(false);
    }
  };

  const handleSeek = (seconds) => {
    if (videoRef.current) {
      videoRef.current.currentTime = seconds;
      videoRef.current.play();
    }
  };

  return (
    <div className="app-container">
      <Navbar />

      <main className="main-content">
        {/* Header */}
        <div style={{ marginBottom: '24px' }}>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '16px' }}>
            <div>
              <h1 className="page-title" style={{ fontSize: '1.8rem', color: 'var(--maroon)' }}>
                🏛️ Swecha Digital Knowledge Archive
              </h1>
              <p className="page-subtitle">
                Multilingual speech transcripts, open audio recordings, and AI-generated village summaries.
              </p>
            </div>
            <button
              className="btn btn-secondary"
              onClick={handleExportCorpus}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: '8px',
                borderColor: 'var(--gold)',
                color: 'var(--ink)',
                fontWeight: '600',
              }}
            >
              📥 Export Telugu Speech Corpus (JSON)
            </button>
          </div>
        </div>

        {/* Search & Filter Bar */}
        <div
          className="card"
          style={{
            padding: '16px 20px',
            marginBottom: '24px',
            display: 'flex',
            gap: '14px',
            flexWrap: 'wrap',
            alignItems: 'center',
          }}
        >
          <div style={{ flex: 1, minWidth: '220px' }}>
            <input
              type="text"
              className="form-input"
              placeholder="🔍 Search across Telugu transcripts, titles, speakers, and topics..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
            />
          </div>

          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <label style={{ fontSize: '0.85rem', fontWeight: 600, color: 'var(--slate)' }}>
              Language:
            </label>
            <select
              className="form-input"
              style={{ width: 'auto', padding: '8px 12px' }}
              value={selectedLanguage}
              onChange={(e) => setSelectedLanguage(e.target.value)}
            >
              <option value="All">All Languages</option>
              <option value="Telugu">Telugu (తెలుగు)</option>
              <option value="English">English</option>
            </select>
          </div>
        </div>

        {loading ? (
          <LoadingSpinner message="Searching bilingual archives..." />
        ) : error ? (
          <div className="error-banner">{error}</div>
        ) : events.length === 0 ? (
          <div className="empty-state card">
            <div className="empty-icon">📂</div>
            <div className="empty-title">No archive recordings matched your search</div>
            <div className="empty-desc">
              Try adjusting your search terms or view upcoming live sessions on the dashboard.
            </div>
          </div>
        ) : (
          <div style={{ display: 'grid', gridTemplateColumns: '320px 1fr', gap: '24px', alignItems: 'start' }}>
            {/* Left Column: Event List */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
              <div style={{ fontSize: '0.9rem', fontWeight: 700, color: 'var(--slate)', textTransform: 'uppercase' }}>
                Archived Sessions ({events.length})
              </div>
              {events.map((ev) => (
                <div
                  key={ev.id}
                  className="card"
                  onClick={() => setSelectedEvent(ev)}
                  style={{
                    padding: '14px 16px',
                    cursor: 'pointer',
                    borderLeft:
                      selectedEvent?.id === ev.id
                        ? '4px solid var(--maroon)'
                        : '1px solid var(--border)',
                    backgroundColor:
                      selectedEvent?.id === ev.id ? '#fff' : '#faf7f2',
                    boxShadow: selectedEvent?.id === ev.id ? '0 4px 12px rgba(122,31,26,0.1)' : 'none',
                  }}
                >
                  <div style={{ fontWeight: 600, fontSize: '0.95rem', color: 'var(--maroon)', marginBottom: '4px' }}>
                    {ev.title}
                  </div>
                  <div style={{ fontSize: '0.78rem', color: 'var(--slate)', marginBottom: '6px' }}>
                    📅 {new Date(ev.scheduled_start).toLocaleDateString([], { month: 'short', day: 'numeric', year: 'numeric' })}
                  </div>
                  <div style={{ display: 'flex', gap: '6px', flexWrap: 'wrap' }}>
                    <span className="badge badge-scheduled" style={{ fontSize: '0.7rem' }}>
                      {ev.language || 'Telugu / English'}
                    </span>
                    {ev.transcript && (
                      <span className="badge badge-success" style={{ fontSize: '0.7rem' }}>
                        ASR Transcript
                      </span>
                    )}
                  </div>
                </div>
              ))}
            </div>

            {/* Right Column: Selected Event Viewer */}
            {selectedEvent && (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
                <div className="card" style={{ padding: '24px' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '16px' }}>
                    <div>
                      <h2 style={{ fontSize: '1.4rem', color: 'var(--ink)', marginBottom: '6px' }}>
                        {selectedEvent.title}
                      </h2>
                      <p style={{ color: 'var(--slate)', fontSize: '0.9rem' }}>
                        {selectedEvent.description || 'Civic-tech session organized by Swecha & Community.'}
                      </p>
                    </div>

                    <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap' }}>
                      <a
                        href={getOfflinePackUrl(selectedEvent.id)}
                        download
                        className="btn btn-secondary"
                        style={{ fontSize: '0.8rem', padding: '6px 12px', textDecoration: 'none', display: 'flex', alignItems: 'center', gap: '6px' }}
                      >
                        📦 Download Offline Pack (.zip)
                      </a>

                      {!selectedEvent.transcript && token && (
                        <button
                          className="btn btn-primary"
                          style={{ fontSize: '0.8rem', padding: '6px 12px' }}
                          onClick={() => handlePopulateDemo(selectedEvent.id)}
                          disabled={actionLoading}
                        >
                          ⚡ Generate Telugu ASR & Summary
                        </button>
                      )}
                    </div>
                  </div>

                  {/* Video Player */}
                  <div style={{ borderRadius: '10px', overflow: 'hidden', backgroundColor: '#000', marginBottom: '20px' }}>
                    <video
                      ref={videoRef}
                      src={selectedEvent.recording_url || 'https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4'}
                      controls
                      style={{ width: '100%', maxHeight: '380px', display: 'block' }}
                      onTimeUpdate={(e) => setCurrentTime(e.target.currentTime)}
                    />
                  </div>

                  {/* AI Summary Section */}
                  {selectedEvent.summary && (
                    <div
                      style={{
                        backgroundColor: '#fef9f1',
                        border: '1px solid var(--gold)',
                        borderRadius: '8px',
                        padding: '16px',
                        marginBottom: '20px',
                      }}
                    >
                      <div style={{ fontWeight: 700, color: 'var(--maroon)', marginBottom: '8px', display: 'flex', alignItems: 'center', gap: '6px' }}>
                        <span>💡</span> AI Executive Summary (తెలుగు / Regional)
                      </div>
                      <div style={{ fontSize: '0.88rem', color: 'var(--ink)', whiteSpace: 'pre-line', lineHeight: 1.6 }}>
                        {selectedEvent.summary}
                      </div>
                    </div>
                  )}

                  {/* Interactive Synchronized Transcript */}
                  <div>
                    <h3 style={{ fontSize: '1.1rem', color: 'var(--ink)', marginBottom: '12px' }}>
                      🎙️ Whisper Multilingual Transcript (Click line to jump video)
                    </h3>

                    {selectedEvent.transcript && Array.isArray(selectedEvent.transcript) ? (
                      <div
                        style={{
                          maxHeight: '320px',
                          overflowY: 'auto',
                          border: '1px solid var(--border)',
                          borderRadius: '8px',
                          backgroundColor: '#faf7f2',
                          padding: '10px',
                          display: 'flex',
                          flexDirection: 'column',
                          gap: '8px',
                        }}
                      >
                        {selectedEvent.transcript.map((seg, idx) => {
                          const isCurrent = currentTime >= seg.start && currentTime <= seg.end;
                          return (
                            <div
                              key={idx}
                              onClick={() => handleSeek(seg.start)}
                              style={{
                                padding: '8px 12px',
                                borderRadius: '6px',
                                backgroundColor: isCurrent ? 'rgba(122, 31, 26, 0.12)' : '#fff',
                                borderLeft: isCurrent ? '3px solid var(--maroon)' : '1px solid #eee',
                                cursor: 'pointer',
                                transition: 'background-color 150ms ease',
                              }}
                            >
                              <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '2px', fontSize: '0.78rem' }}>
                                <span style={{ fontWeight: 600, color: 'var(--maroon)' }}>
                                  {seg.speaker || 'Speaker'}
                                </span>
                                <span style={{ color: 'var(--slate)' }}>
                                  ⏱️ {Math.floor(seg.start)}s - {Math.floor(seg.end)}s
                                </span>
                              </div>
                              <div style={{ fontSize: '0.88rem', color: 'var(--ink)', lineHeight: 1.4 }}>
                                {seg.text}
                              </div>
                            </div>
                          );
                        })}
                      </div>
                    ) : (
                      <p style={{ color: 'var(--slate)', fontSize: '0.88rem', fontStyle: 'italic' }}>
                        No transcript generated yet. Click "Generate Telugu ASR" above to simulate automated Whisper transcription.
                      </p>
                    )}
                  </div>
                </div>
              </div>
            )}
          </div>
        )}
      </main>
    </div>
  );
}
