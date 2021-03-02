import request from '@/utils/request'

export function postQuestionnaire(questionnaire) {
  return request({
    url: '/questionnaire/create',
    method: 'post',
    data: questionnaire
  })
}

export function getQuestionnaireList(patientId) {
  return request({
    url: '/questionnaire/get/list/' + patientId,
    method: 'get'
  })
}

