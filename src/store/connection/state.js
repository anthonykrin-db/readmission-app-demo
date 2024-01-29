export default function () {
  return {
    //  ////////////////////
    // CONNECTION
    //  ////////////////////
    client: null,
    refreshRate: 0,
    message: 'NOT CONNECTED',
    timestamp: 0,
    errorCode: 0,
    errorMessage: '',
    connected: false,
    loggedIn: false,
    pauseCheck: false
  }
}
