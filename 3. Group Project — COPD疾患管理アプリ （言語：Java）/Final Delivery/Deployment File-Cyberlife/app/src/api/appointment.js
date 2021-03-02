import request from '@/utils/request'

export function postAppointment(appointment) {
  return request({
    url: '/appointment/create',
    method: 'post',
    data: appointment
  })
}

export function updateAppointmentStatus(appointmentId, status) {
  return request({
    url: '/appointment/update/status/' + appointmentId,
    method: 'post',
    params: {
      status: status
    }
  })
}

export function getAppointmentByDoctorId(doctorId) {
  return request({
    url: '/appointment/get/doctor/' + doctorId,
    method: 'get'
  })
}

export function getAppointmentByPatientId(patientId) {
  return request({
    url: '/appointment/get/patient/' + patientId,
    method: 'get'
  })
}
