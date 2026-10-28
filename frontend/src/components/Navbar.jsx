import { useState } from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import WhatsAppSimulator from './WhatsAppSimulator';

export default function Navbar() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();
  const [showWhatsApp, setShowWhatsApp] = useState(false);

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <>
      <header className="navbar">
        <div style={{ display: 'flex', alignItems: 'center', gap: '20px' }}>
          <Link to="/dashboard" style={{ textDecoration: 'none', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <span className="navbar-brand">🚩 Swecha Vedika</span>
            <span className="navbar-brand-badge">CIVIC STAGE</span>
          </Link>

          {/* Navigation Links */}
          {user && (
            <nav style={{ display: 'flex', gap: '12px', alignItems: 'center' }}>
              <Link
                to="/dashboard"
                style={{
                  color: location.pathname === '/dashboard' ? 'var(--maroon)' : 'var(--slate)',
                  fontWeight: location.pathname === '/dashboard' ? 700 : 500,
                  fontSize: '0.9rem',
                  textDecoration: 'none',
                  padding: '4px 8px',
                  borderRadius: '6px',
                  backgroundColor: location.pathname === '/dashboard' ? 'rgba(122,31,26,0.08)' : 'transparent',
                }}
              >
                Dashboard
              </Link>
              <Link
                to="/archive"
                style={{
                  color: location.pathname === '/archive' ? 'var(--maroon)' : 'var(--slate)',
                  fontWeight: location.pathname === '/archive' ? 700 : 500,
                  fontSize: '0.9rem',
                  textDecoration: 'none',
                  padding: '4px 8px',
                  borderRadius: '6px',
                  backgroundColor: location.pathname === '/archive' ? 'rgba(122,31,26,0.08)' : 'transparent',
                }}
              >
                🏛️ Archive (తెలుగు)
              </Link>
            </nav>
          )}
        </div>

        {user && (
          <div className="navbar-user-section" style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
            {/* WhatsApp Bot Launcher */}
            <button
              className="btn"
              style={{
                fontSize: '0.8rem',
                padding: '5px 12px',
                backgroundColor: '#075e54',
                color: '#fff',
                border: 'none',
                display: 'flex',
                alignItems: 'center',
                gap: '6px',
                borderRadius: '16px',
              }}
              onClick={() => setShowWhatsApp(true)}
              title="Open Swecha WhatsApp Bot Simulator"
            >
              <span>💬</span> WhatsApp Bot
            </button>

            <span className="navbar-username">{user.name}</span>
            <span className="navbar-role-pill">{user.role}</span>
            <button
              className="btn btn-nav-logout"
              onClick={handleLogout}
              title="Log out of Swecha Vedika"
            >
              Logout
            </button>
          </div>
        )}
      </header>

      {/* WhatsApp Simulator Popup */}
      <WhatsAppSimulator
        isOpen={showWhatsApp}
        onClose={() => setShowWhatsApp(false)}
      />
    </>
  );
}
