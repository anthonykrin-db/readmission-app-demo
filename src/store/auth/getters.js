
export function username(state){
  return state.username
}

export function userProfile (state) {
  return state.profile
}
export function currentToken (state) {
  if (state.token === null || state.token === undefined || state.token === '') return null
  return state.token
}
export function devFooter (state) {
  return 'token: ' + (state.token === null ? 'GUEST' : state.token).substr(0, 10) + '... username:' +
    (state.username === null ? 'ANONYMOUS' : state.username) + '... ' + ',  restApiUri: ' + process.env.REST_API_URI
}
export function loggedIn (state) {
  return !(state.username === '')
}
export function axiosAuthHeader (state) {
  return { headers: { 'X-Authorization': 'Bearer: ' + state.token } }
}

export function requestHeader (state, getters, rootState, rootGetters) {
  var requestHeader = new RequestHeader()
  // Beware that all rootGetters are global and you no longer use it like rootState where you would prefix the state by the module name.
  requestHeader.setAuthtoken(getters.currentToken)
  requestHeader.setCreatedts(getters.utcTsMs)
  return requestHeader
}

export function utcTsMs (state) {
  var d = new Date()
  return Date.UTC(d.getUTCFullYear(), d.getUTCMonth() + 1, d.getUTCDate(), d.getUTCHours(), d.getUTCMinutes(), d.getUTCSeconds(), d.getUTCMilliseconds())
}
