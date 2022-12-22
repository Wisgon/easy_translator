import { useCallback } from 'react';
import {
  MemoryRouter as Router,
  Routes,
  Route,
  useNavigate,
} from 'react-router-dom';
import icon from '../../assets/icon.svg';
import './App.css';
import Collections from './pages/collections/collections';

const Hello = () => {
  const openSettingsWindow = useCallback(() => {
    window.electron.ipcRenderer.openSettingsWindow();
  }, []);
  const navigate = useNavigate(); // use to switch page
  return (
    <div>
      <div className="Hello">
        <img width="200" alt="icon" src={icon} />
      </div>
      <h1>electron-react-boilerplate</h1>
      <div className="Hello">
        <button type="button" onClick={openSettingsWindow}>
          <span role="img" aria-label="gear">
            ⚙️
          </span>
          Open Settings
        </button>

        <button type="button" onClick={() => navigate('/collections')}>
          <span role="img" aria-label="books">
            📚
          </span>
          Read our docs
        </button>
      </div>
    </div>
  );
};

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Hello />} />
        <Route path="/collections" element={<Collections />} />
      </Routes>
    </Router>
  );
}
