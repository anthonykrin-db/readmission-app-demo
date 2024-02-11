import {defineStore} from 'pinia'
import axios from "axios";
import {useQuasar} from "quasar";

export const useAuthStore = defineStore('auth', {
  state: () => ({
    isAuthenticated: false,
    username: '',
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
        axios.post('api/auth/authenticate', credentials)
          .then(response => {
            const tkn = response.data.token;
            if (tkn) {
              console.log("REST authenticate: Got token")
              this.token = tkn;
              this.username = credentials.username;
              this.isAuthenticated = true;
              resolve(true); // Login successful
            } else {
              resolve(false); // Login unsuccessful
            }
          })
          .catch(error => {
            console.error('REST authenticate error:', error);
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
            console.error('Logout failed:', error);
            reject(error);
          });
      });
    },
    usernameExists(userName) {
      return axios.get('api/auth/username-exists/' + userName)
    },
    updateProfile(profile) {
      context.dispatch('checkLogin')
      this.profile = profile
      return axios.put('api/auth/profile', profile, context.getters.axiosAuthHeader)
    },
    getProfile() {
      context.dispatch('checkLogin')
      return axios.get('api/auth/profile', context.getters.axiosAuthHeader)
    }
  }
})
