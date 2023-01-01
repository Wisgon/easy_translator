// import { useCallback } from 'react';
// import {
//   MemoryRouter as Router,
//   Routes,
//   Route,
//   useNavigate,
// } from 'react-router-dom';
// import icon from '../../assets/icon.svg';
// import './App.css';
// import Collections from './pages/collections/collections';

// const Hello = () => {
//   const openSettingsWindow = useCallback(() => {
//     window.electron.ipcRenderer.openSettingsWindow();
//   }, []);
//   const navigate = useNavigate(); // use to switch page
//   return (
//     <div>
//       <div className="Hello">
//         <img width="200" alt="icon" src={icon} />
//       </div>
//       <h1>electron-react-boilerplate</h1>
//       <div className="Hello">
//         <button type="button" onClick={openSettingsWindow}>
//           <span role="img" aria-label="gear">
//             ⚙️
//           </span>
//           Open Settings
//         </button>

//         <button type="button" onClick={() => navigate('/collections')}>
//           <span role="img" aria-label="books">
//             📚
//           </span>
//           Read our docs
//         </button>
//       </div>
//     </div>
//   );
// };

// export default function App() {
//   return (
//     <Router>
//       <Routes>
//         <Route path="/" element={<Hello />} />
//         <Route path="/collections" element={<Collections />} />
//       </Routes>
//     </Router>
//   );
// }

import React from 'react';
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
