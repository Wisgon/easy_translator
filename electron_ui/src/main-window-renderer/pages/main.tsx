import { Button, DatePicker, Space } from 'antd';
import 'antd/dist/antd.css';
import sendMsg from '../../websocket/client';

function sendTranslateRequest() {
  // todo:get input data
  const input = 'xxx';
  sendMsg({
    type: 'input_translate',
    data: { value: input },
  });
}

const MainPage = () => {
  return (
    <div>
      <h1>main</h1>
      <Space>
        <DatePicker />
        <Button type="primary" onClick={sendTranslateRequest}>
          Primary Button
        </Button>
      </Space>
    </div>
  );
};

export default MainPage;
