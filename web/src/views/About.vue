<template>
  <div class="about">
    <h1>This is an about page</h1>
    <el-button type="text" @click="handleClose"
      >click to open the test</el-button
    >
    <div>{{ user }}</div>
    <div>{{ results }}</div>
  </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  data() {
    return {
      results: [],
    };
  },
  computed: mapState({
    user: (state) => state.user,
  }),
  mounted() {
    // const socket = io(`http://127.0.0.1:${parseInt(window.location.port, 10) - 1}/`, { transports: ['polling', 'flashsocket'], path: '/ws' });
    this.$socket.client.on('pong', (payload) => {
      console.log('pong', payload);
      this.results.push(payload);
      this.$socket.client.emit('ping', { status: Date.now });
    });
  },
  methods: {
    handleClose(done) {
      console.log(this.$socket.client);
      this.$socket.client.emit('ping', { status: Date.now });
      this.$store.dispatch('user/login');
    },
  },
};
</script>
