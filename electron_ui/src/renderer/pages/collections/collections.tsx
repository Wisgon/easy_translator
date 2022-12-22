import { Button, DatePicker, Space, version } from 'antd';
import 'antd/dist/antd.css';

const Colllections = () => {
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

export default Colllections;
