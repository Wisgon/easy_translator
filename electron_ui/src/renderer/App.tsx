import { useEffect } from 'react';
import './App.css';
import 'antd/dist/antd.css';
import { useNavigate } from 'react-router-dom';
import { Layout, Menu } from 'antd';
import RouterDom from './router';

interface Item {
  label: string;
  key: string;
  children: Item[] | null;
}

function getItem(label: string, key: string, children: Item[] | null): Item {
  return {
    label,
    key,
    children,
  };
}

const { Content, Footer, Sider } = Layout;

const menuItems = [
  getItem('MainPage', '/main', null),
  getItem('Setting', '', [getItem('Collection', '/collections', null)]),
];

export default function App() {
  const navigate = useNavigate(); // use to switch page
  const onClick = (e: any) => {
    navigate(e.key, { replace: true });
  };
  useEffect(() => {
    navigate('/main', { replace: true });
  }, []); // the '[]' argument informs the useEffect hook that it only be executed just once.
  return (
    <Layout>
      <Sider
        breakpoint="lg"
        collapsedWidth="0"
        onBreakpoint={(broken) => {
          console.log(broken);
        }}
        onCollapse={(collapsed, type) => {
          console.log(collapsed, type);
        }}
      >
        <div className="logo" />
        <Menu
          theme="dark"
          defaultSelectedKeys={['/main']}
          mode="inline"
          items={menuItems}
          onClick={onClick}
        />
      </Sider>
      <Layout>
        {/* <Header
        className="site-layout-sub-header-background"
        style={{ padding: 0 }}
      /> */}
        <Content
          className="site-layout-background"
          style={{
            margin: '24px 16px',
            padding: 24,
            minHeight: 280,
          }}
        >
          <RouterDom />
        </Content>
        <Footer style={{ textAlign: 'center' }}>Easy Translator V1.0</Footer>
      </Layout>
    </Layout>
  );
}
