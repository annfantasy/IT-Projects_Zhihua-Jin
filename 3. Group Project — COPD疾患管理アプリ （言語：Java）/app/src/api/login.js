import request from '@/utils/request'

export function login(username, password) {
  return request({
    url: '/login',
    method: 'post',
    data: {
      username,
      password
    }
  })
}

export function register(registerForm) {
  return request({
    url: '/user/create',
    method: 'post',
    data: registerForm
  })
}

export function getInfo() {
  return request({
    url: '/user/get/info',
    method: 'get'
  })
}

export function logout() {
  return request({
    url: '/logout',
    method: 'post'
  })
}
