

import axios from 'axios'
import { Notify } from 'quasar'


export function saveSurveyMetadata (context, survey) {
  // console.log('Axios header: ' + JSON.stringify(context.rootGetters['auth/axiosAuthHeader']))
  if (survey.surveyId === null || survey.surveyId === '') {
    return axios.post('api/survey/create', survey, context.rootGetters['auth/axiosAuthHeader'])
  } else {
    return axios.put('api/survey/update', survey, context.rootGetters['auth/axiosAuthHeader'])
  }
}

export function invitePlayers (context, surveyId, playersList) {
  return axios.post('api/survey/invite/' + surveyId, playersList, context.rootGetters['auth/axiosAuthHeader'])
}

export function checkActivesurvey (context) {
  if (context.playing.survey === null || context.playing.survey === '' || context.playing.survey === undefined) {
    this.dispatch('routePage', 'surveys')
    return false
  } else if (context.editing.survey === null || context.editing.survey === '' || context.editing.survey === undefined) {
    this.dispatch('routePage', 'surveys')
    return false
  }
  return true
}
