export function updateConnection (state, client) {
  if (client == null) {
    // state.streamingClient = null
    console.log('Not updating client to null.')
  } else {
    state.client = client
  }
  console.log('Updating connection with client: ', state.client)
}


// client: null,
//     refreshRate: 0,
//     error: '',
//     connected: false,
//     loggedIn: false
export function updatePingSuccess (state, pingResponse) {
  console.log('Update ping success.')
  state.message = pingResponse.getMessage()
  state.timestamp = pingResponse.getTimestamp()
  state.connected = true
}

export function updatePingFail (state, err) {
  console.log('Update ping fail.')
  state.message = null
  state.timestamp = 0
  state.connected = false
  if (err != null) {
    state.errorCode = err.code
    state.errorMessage = err.message
  }
  // TODO: reconnect if failure?
}

export function updatePauseCheck (state, pause) {
  console.log('Updating updatePauseCheck: ', pause)
  state.pauseCheck = pause
}

