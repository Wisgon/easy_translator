import { Button, DatePicker, Space } from 'antd';
import 'antd/dist/antd.css';

const Colllections = () => {
  return (
    <div>
      <h1>Collection</h1>
      <Space>
        <DatePicker />
        <Button type="primary">Primary Button</Button>
      </Space>
    </div>
  );
};

export default Colllections;
