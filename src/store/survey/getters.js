export function surveyId (state) {
  return state.surveyId
}

export function createGuid (state) {
  function s4 () {
    return Math.floor((1 + Math.random()) * 0x10000).toString(16).substring(1)
  }
  return s4() + s4() + '-' + s4() + '-' + s4() + '-' + s4() + '-' + s4() + s4() + s4()
}


export function returnToUrl (state, getters, rootState, rootGetters) {
  return rootGetters.returnToUrl(rootState)
}
