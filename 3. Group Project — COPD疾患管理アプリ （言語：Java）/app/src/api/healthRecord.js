import request from '@/utils/request'

export function postHealthRecord(healthRecord) {
  return request({
    url: '/record/create',
    method: 'post',
    data: healthRecord
  })
}

export function getHealthRecordList(patientId) {
  return request({
    url: '/record/get/list/' + patientId,
    method: 'get'
  })
}

