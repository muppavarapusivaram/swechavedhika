import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

export default function Navbar() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <header className="navbar">
      <div className="navbar-brand">
        <span>Swecha Vedika</span>
        <span className="navbar-brand-badge">PROTOTYPE</span>
      </div>

      {user && (
        <div className="navbar-user-section">
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
  );
}
