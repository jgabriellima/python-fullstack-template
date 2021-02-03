import { Module } from 'vuex';
import userservice from '../../api/user';
import constants from '../../api/constants';

// getters
const getters = {};

// actions
const actions = {
  login({ commit }: { commit: Function }) {
    userservice.login().then((user: any) => {
      console.log('LOGIN ACTION', user);
      commit(constants.SET_USER, user);
    });
  },
};

// mutations
const mutations = {
  setUser(state: any, user: any) {
    state.user = user;
  },
};

// initial state
const state = () => ({
  user: {},
});

const userModule: Module<any, any> = {
  namespaced: true,
  state,
  mutations,
  actions,
  getters,
};

export default userModule;
