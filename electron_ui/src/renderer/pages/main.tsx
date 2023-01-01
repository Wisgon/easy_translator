import { Button, DatePicker, Space } from 'antd';
import 'antd/dist/antd.css';

const MainPage = () => {
  return (
    <div>
      <h1>main</h1>
      <Space>
        <DatePicker />
        <Button type="primary">Primary Button</Button>
      </Space>
    </div>
  );
};

export default MainPage;
