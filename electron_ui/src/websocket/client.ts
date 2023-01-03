import { WebsocketBuilder } from 'websocket-ts';

const port = 5679;

const ws = new WebsocketBuilder(`ws://localhost:${port}`)
  .onMessage((i, ev) => {
    // ev.data is the data that server sended.
    console.log(ev.data);
    window.electron.ipcRenderer.openbuttonWindow();
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
