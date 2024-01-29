/*
export function someMutation (state) {
}
*/

import Vue from 'vue'


export function mutateSurvey (state, survey) {
  state.surveyId = survey.surveyId
  state.questions = survey.questions
}

export function mutateResponses (state, responses) {
  state.responses = survey.responses
}
