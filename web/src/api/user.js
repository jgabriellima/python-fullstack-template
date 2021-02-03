import constants from './constants';

export default {
  login() {
    console.log(constants.URL);
    return Promise.resolve({ username: 'joaogabriellima', password: '12345678' });
  },
};
