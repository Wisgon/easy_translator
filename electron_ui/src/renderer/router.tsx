import { Routes, Route } from 'react-router-dom';
import Collections from './pages/collections';
import MainPage from './pages/main';

export default function RouterDom() {
  return (
    <div>
      <Routes>
        <Route path="/main" element={<MainPage />} />
        <Route path="/collections" element={<Collections />} />
      </Routes>
    </div>
  );
}
