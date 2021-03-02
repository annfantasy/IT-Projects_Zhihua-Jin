import request from '@/utils/request'

export function getDoctorList() {
  return request({
    url: '/doctor/get/list',
    method: 'get'
  })
}

