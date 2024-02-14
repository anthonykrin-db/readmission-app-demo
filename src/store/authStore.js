import {defineStore} from 'pinia';
//import {axios} from "../store/axiosClient";
import axios from 'axios'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    isAuthenticated: false,
    username: 'Guest',
    token: '',
    profile: {}
  }),
  getters: {
    axiosAuthHeader(state) {
      return {headers: {'X-Authorization': 'Bearer: ' + state.token}}
    },
    debugFooter(state) {
      return state.username + "/" + state.token
    }
  },
  actions: {
    login(credentials) {
      return new Promise((resolve, reject) => {
        axios.post('api/auth/login', credentials)
          .then(response => {
            const tkn = response.data.token;
            const msg = response.data.message;
            if (tkn) {
              console.log("REST authenticate: Got token: "+tkn+", msg: "+msg)
              this.token = tkn;
              this.username = credentials.username;
              this.isAuthenticated = true;
              resolve(true); // Login successful
            } else {
              resolve(false); // Login unsuccessful
            }
          })
          .catch(error => {
            console.log('REST authenticate error:', error);
            reject(error);
          });
      });
    },

    logout() {
      // Perform your logout logic here
      // For simplicity, let's just set isAuthenticated to false
      return new Promise((resolve, reject) => {
        axios.post('api/auth/logout')
          .then(response => {
            this.token = "";
            this.username="Guest";
            this.isAuthenticated = false;
            resolve(true); // Login successful
          })
          .catch(error => {
            console.log('REST logout failed:', error);
            reject(error);
          });
      });
    }
  }
})
