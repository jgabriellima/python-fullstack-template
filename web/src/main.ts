import { createApp } from 'vue';
import ElementPlus from 'element-plus';
import VueSocketIOExt from 'vue-socket.io-extended';
import { io } from 'socket.io-client';

import App from './App.vue';
import './registerServiceWorker';
import router from './router';
import store from './store';
import 'element-plus/lib/theme-chalk/index.css';

console.log('process.env.NODE_ENV: ', process.env.NODE_ENV);
console.log('process.env.API_PORT: ', process.env.VUE_APP_API_PORT);
console.log('process.env.SOCKET_PORT: ', process.env.VUE_APP_SOCKET_PORT);
// console.log(`http://localhost:${parseInt(window.location.port, 10) - 1}/`);
let socket = null;
if (process.env.NODE_ENV !== 'production') {
  socket = io(`http://127.0.0.1:${process.env.VUE_APP_SOCKET_PORT}/`, { transports: ['polling', 'flashsocket'], path: '/socket.io' });
} else {
  socket = io({ transports: ['polling', 'flashsocket'], path: '/socket.io' });
}

const app = createApp(App).use(ElementPlus).use(store)
  .use(VueSocketIOExt, socket, { store })
  .use(router)
  .mount('#app');
