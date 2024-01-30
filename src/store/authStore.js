import { defineStore } from 'pinia'
import axios from "axios";
import {useQuasar} from "quasar";
export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: 'xyz',
    username: 'Guest',
    profile: {},
    redirectAfterLogin: '',
    registrationResponse: ''
  }),
  getters: {
    axiosAuthHeader (state) {
      return { headers: { 'X-Authorization': 'Bearer: ' + state.token } }
    },
    debugFooter (state) {
      return state.username+"/"+state.token
    }
  },
  actions: {
    login (context, authCredential) {
      return axios.post('api/auth/authenticate', authCredential)
    },
    usernameExists (context, userName) {
      return axios.get('api/auth/username-exists/' + userName)
    },
    updateProfile (context, profile) {
      context.dispatch('checkLogin')
      this.profile = profile
      return axios.put('api/auth/profile', profile, context.getters.axiosAuthHeader)
    },
    getProfile (context) {
      context.dispatch('checkLogin')
      return axios.get('api/auth/profile', context.getters.axiosAuthHeader)
    }
  }
})
