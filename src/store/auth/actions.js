/*
export function someAction (context) {
}
*/
import axios from 'axios'

export function login (context, authCredential) {
  return axios.post('api/auth/authenticate', authCredential)
}

export function usernameExists (context, userName) {
  return axios.get('api/auth/username-exists/' + userName)
}

export function updateProfile (context, profile) {
  context.dispatch('checkLogin')
  return axios.put('api/auth/profile', profile, context.getters.axiosAuthHeader)
}

export function getProfile (context) {
  context.dispatch('checkLogin')
  return axios.get('api/auth/profile', context.getters.axiosAuthHeader)
}

export function updatePreferences (context, preferences) {
  context.dispatch('checkLogin')
  return axios.put('api/auth/preferences', preferences, context.getters.axiosAuthHeader)
}

export function updatePassword (context, password) {
  context.dispatch('checkLogin')
  return axios.put('api/auth/password', password, context.getters.axiosAuthHeader)
}

export function resetAuth (context) {
  context.commit('mutateClearAuth')
}

export function register (context, registerUser) {
  return axios.post('api/auth/register', registerUser)
    .then(res => {
      console.log('Axios response: ' + JSON.stringify(res))
      return res
    })
    .catch((error) => {
      console.log('Error on server registering user: ' + error)
      return error
    })
    .finally()
}

export function checkLogin (context, returnToUrl) {
  console.log('Checking login with return to url: ' + returnToUrl)
  if (context.getters.currentToken === null || context.getters.currentToken === '' || context.getters.currentToken === undefined) {
    this.dispatch('routePage', { pageName: 'login', url: returnToUrl })
    return false
  }
  return true
}
