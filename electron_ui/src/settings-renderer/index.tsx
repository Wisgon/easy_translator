import { createRoot } from 'react-dom/client';
import { Button, DatePicker, Space, version } from 'antd';
import 'antd/dist/antd.css';

const App = () => {
  return (
    <div>
      <h1>antd version: {version}</h1>
      <Space>
        <DatePicker />
        <Button type="primary">Primary Button</Button>
      </Space>
    </div>
  );
};

const container = document.getElementById('root')!;
const root = createRoot(container);
root.render(<App />);
