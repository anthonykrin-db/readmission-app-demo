export function mutatePatient(state, profile) {
  state.salutation = profile.salutation
  state.name = profile.name
  state.patientid = profile.patientid
  state.welcomemsg = profile.welcomemsg
  state.numUnreadTasks = profile.numUnreadTasks
  state.numUnreadAlerts = profile.numUnreadAlerts
  state.numNewResources = profile.numNewResources
  state.numNewTimeline = profile.numNewTimeline
}
