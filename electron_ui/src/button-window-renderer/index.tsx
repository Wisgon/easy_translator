import { createRoot } from 'react-dom/client';
import { Button } from 'antd';
import 'antd/dist/antd.css';

const App = () => {
  return (
    <div>
      <Button type="primary">Primary Button</Button>
    </div>
  );
};

const container = document.getElementById('root')!;
const root = createRoot(container);
root.render(<App />);
