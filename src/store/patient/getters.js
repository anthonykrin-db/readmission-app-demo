export function tableBBox (state) {
  return state.tableBBox
}
export function playersPositions (state) {
  return state.positions.players
}
export function playerPosition (state, playerId) {
  return state.positions.players[playerId]
}
export function cardDims (state) {
  return state.cardDims
}
export function playerSvgAnchors (state) {
  return state.playerSvgAnchors
}
export function playerScreenAnchors (state) {
  return state.playerScreenAnchors
}
export function orientedPlayers (state) {
  return state.orientedPlayers
}
export function numPlayers (state) {
  return state.numPlayers
}
export function commandBarOpen (state) {
  return state.commandBarOpen
}
export function bankOpen (state) {
  return state.bankOpen
}
export function currentPlayerId (state) {
  // todo: rework this to get from survey module...
  return state.playerId
}
export function buttonOnId (state) {
  return state.buttonOnId
}
export function players (state) {
  return state.players
}
export function decks (state) {
  return state.decks
}
