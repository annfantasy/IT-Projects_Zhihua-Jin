import request from '@/utils/request'

export function postArticle(article) {
  return request({
    url: '/article/create',
    method: 'post',
    data: article
  })
}

export function getArticleList() {
  return request({
    url: '/article/get/list',
    method: 'get'
  })
}

export function getArticle(articleId) {
  return request({
    url: '/article/get/' + articleId,
    method: 'get'
  })
}
