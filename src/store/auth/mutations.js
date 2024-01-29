

export function mutateClearAuth (state) {
  state.username = ''
  state.profile = {}
  state.token = ''
}
export function mutateUser (state, username) {
  state.username = username
}

export function mutateToken (state, token) {
  state.token = token
}

export function mutateProfile (state, profile) {
  state.profile = profile
}
