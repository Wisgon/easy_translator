import { WebsocketBuilder } from 'websocket-ts';

const port = 5679;

const ws = new WebsocketBuilder(`ws://localhost:${port}`)
  .onOpen((i, ev) => {
    console.log('opened');
  })
  .onMessage((i, ev) => {
    // ev.data is the data that server sended.
    console.log(ev.data);
    const data = JSON.parse(ev.data);
    switch (data.msg) {
      case 'selected word': // selected word,open button window
        window.electron.ipcRenderer.openbuttonWindow(data.data.x, data.data.y);
        break;
      default:
        console.log('not match msg');
        break;
    }
  })
  .onError((i, ev) => {
    console.log('error', ev, i);
  })
  .build();

function sendMsg(data: object) {
  // data must be like {type: 'xxx', data: {yyy:zzz}}
  ws.send(JSON.stringify(data));
}

// ws.onOpen((i, ev) => {
//   console.log('opened');
// })
//   .onClose((i, ev) => {
//     console.log('closed');
//   })
//   .onError((i, ev) => {
//     console.log('error');
//   })
//   .onMessage((i, ev) => {
//     console.log('message');
//   })
//   .onRetry((i, ev) => {
//     console.log('retry');
//   });

export default sendMsg;
