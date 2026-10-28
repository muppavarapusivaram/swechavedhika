import { useState } from 'react';
import { simulateWhatsApp } from '../api/client';

export default function WhatsAppSimulator({ isOpen, onClose, currentEventId }) {
  const [messages, setMessages] = useState([
    {
      id: 1,
      sender: 'bot',
      text: 'నమస్కారం! Welcome to Swecha Vedika WhatsApp Service.\nSend *EVENTS* to see upcoming live sessions, or *RSVP* to confirm attendance.',
      time: '10:00 AM',
    },
  ]);
  const [inputText, setInputText] = useState('');
  const [loading, setLoading] = useState(false);
  const [phone, setPhone] = useState('+919876543210');

  if (!isOpen) return null;

  const handleSend = async (customText = null) => {
    const textToSend = customText || inputText;
    if (!textToSend.trim() || loading) return;

    const userMsg = {
      id: Date.now(),
      sender: 'user',
      text: textToSend,
      time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
    };

    setMessages((prev) => [...prev, userMsg]);
    if (!customText) setInputText('');
    setLoading(true);

    try {
      const res = await simulateWhatsApp(textToSend, phone, 'Village Volunteer');
      const botMsg = {
        id: Date.now() + 1,
        sender: 'bot',
        text: res.reply,
        time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      };
      setMessages((prev) => [...prev, botMsg]);
    } catch {
      setMessages((prev) => [
        ...prev,
        {
          id: Date.now() + 1,
          sender: 'bot',
          text: '❌ Could not connect to WhatsApp webhook service.',
          time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        position: 'fixed',
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
        backgroundColor: 'rgba(43, 33, 26, 0.6)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        zIndex: 1000,
        padding: '16px',
      }}
      onClick={onClose}
    >
      <div
        style={{
          width: '100%',
          maxWidth: '430px',
          height: '620px',
          backgroundColor: '#efeae2',
          borderRadius: '18px',
          boxShadow: '0 12px 36px rgba(0,0,0,0.3)',
          display: 'flex',
          flexDirection: 'column',
          overflow: 'hidden',
          border: '1px solid #d1d7db',
        }}
        onClick={(e) => e.stopPropagation()}
      >
        {/* WhatsApp Header */}
        <div
          style={{
            backgroundColor: '#075e54',
            color: '#fff',
            padding: '12px 16px',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
            <div
              style={{
                width: '38px',
                height: '38px',
                borderRadius: '50%',
                backgroundColor: 'var(--gold)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontWeight: 'bold',
                color: '#fff',
              }}
            >
              🚩
            </div>
            <div>
              <div style={{ fontWeight: '600', fontSize: '0.95rem' }}>
                Swecha Vedika Bot
              </div>
              <div style={{ fontSize: '0.75rem', opacity: 0.85 }}>
                Official Automated Helpline • Online
              </div>
            </div>
          </div>
          <button
            onClick={onClose}
            style={{
              background: 'none',
              border: 'none',
              color: '#fff',
              fontSize: '1.4rem',
              cursor: 'pointer',
              lineHeight: 1,
            }}
          >
            ×
          </button>
        </div>

        {/* Quick action chips */}
        <div
          style={{
            padding: '8px 12px',
            backgroundColor: '#fff',
            borderBottom: '1px solid #e0e0e0',
            display: 'flex',
            gap: '8px',
            overflowX: 'auto',
          }}
        >
          <button
            className="btn btn-secondary"
            style={{ fontSize: '0.75rem', padding: '4px 10px', whiteSpace: 'nowrap' }}
            onClick={() => handleSend('EVENTS')}
          >
            📅 EVENTS
          </button>
          {currentEventId && (
            <button
              className="btn btn-secondary"
              style={{ fontSize: '0.75rem', padding: '4px 10px', whiteSpace: 'nowrap' }}
              onClick={() => handleSend(`RSVP ${currentEventId.slice(0, 8)}`)}
            >
              🎟️ RSVP Now
            </button>
          )}
          {currentEventId && (
            <button
              className="btn btn-secondary"
              style={{ fontSize: '0.75rem', padding: '4px 10px', whiteSpace: 'nowrap' }}
              onClick={() => handleSend(`ASK ${currentEventId.slice(0, 8)}: నమస్కారం! Low data mode demo question.`)}
            >
              ❓ Ask Live Question
            </button>
          )}
          <button
            className="btn btn-secondary"
            style={{ fontSize: '0.75rem', padding: '4px 10px', whiteSpace: 'nowrap' }}
            onClick={() => handleSend('SUMMARY')}
          >
            📋 AI Summary
          </button>
        </div>

        {/* Chat message history */}
        <div
          style={{
            flex: 1,
            padding: '16px',
            overflowY: 'auto',
            display: 'flex',
            flexDirection: 'column',
            gap: '12px',
            backgroundImage: 'radial-gradient(#d6cdb7 1px, transparent 1px)',
            backgroundSize: '16px 16px',
          }}
        >
          {messages.map((m) => (
            <div
              key={m.id}
              style={{
                alignSelf: m.sender === 'user' ? 'flex-end' : 'flex-start',
                maxWidth: '82%',
                backgroundColor: m.sender === 'user' ? '#dcf8c6' : '#ffffff',
                padding: '10px 12px',
                borderRadius:
                  m.sender === 'user'
                    ? '10px 10px 2px 10px'
                    : '10px 10px 10px 2px',
                boxShadow: '0 1px 2px rgba(0,0,0,0.12)',
                fontSize: '0.875rem',
                color: '#111',
                whiteSpace: 'pre-line',
              }}
            >
              <div>{m.text}</div>
              <div
                style={{
                  textAlign: 'right',
                  fontSize: '0.68rem',
                  color: '#667781',
                  marginTop: '4px',
                }}
              >
                {m.time}
              </div>
            </div>
          ))}
          {loading && (
            <div
              style={{
                alignSelf: 'flex-start',
                backgroundColor: '#fff',
                padding: '8px 14px',
                borderRadius: '12px',
                fontSize: '0.8rem',
                color: 'var(--slate)',
                fontStyle: 'italic',
              }}
            >
              Typing...
            </div>
          )}
        </div>

        {/* Input Bar */}
        <div
          style={{
            padding: '10px 12px',
            backgroundColor: '#f0f2f5',
            display: 'flex',
            alignItems: 'center',
            gap: '8px',
          }}
        >
          <input
            type="text"
            className="form-input"
            style={{
              flex: 1,
              backgroundColor: '#fff',
              fontSize: '0.875rem',
              padding: '8px 12px',
              borderRadius: '20px',
            }}
            placeholder="Type WhatsApp message..."
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && handleSend()}
          />
          <button
            className="btn btn-primary"
            style={{
              padding: '8px 14px',
              borderRadius: '20px',
              fontSize: '0.85rem',
            }}
            onClick={() => handleSend()}
            disabled={loading}
          >
            Send
          </button>
        </div>
      </div>
    </div>
  );
}
