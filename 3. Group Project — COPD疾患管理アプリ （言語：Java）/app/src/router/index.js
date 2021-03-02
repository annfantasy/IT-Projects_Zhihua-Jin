import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '../views/layout/Layout'

export const constantRouterMap = [
  { path: '/login', component: () => import('@/views/login/index'), hidden: true },
  { path: '/404', component: () => import('@/views/404'), hidden: true },

  {
    path: '/',
    component: Layout,
    redirect: '/home',
    name: 'home',
    hidden: true,
    children: [{
      path: 'home',
      component: () => import('@/views/home/index')
    }]
  },

  {
    path: '/article/:id',
    name: 'Article',
    component: () => import('@/views/article/index'),
    meta: { title: 'Article' }
  },

  {
    path: '/health',
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'health',
        component: () => import('@/views/health/index'),
        meta: { title: 'Health' }
      }
    ]
  },

  {
    path: '/schedule',
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'schedule',
        component: () => import('@/views/schedule/index'),
        meta: { title: 'Schedule' }
      }
    ]
  },

  {
    path: '/data',
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'data',
        component: () => import('@/views/data/index'),
        meta: { title: 'Data' }
      }
    ]
  },

  {
    path: '/mine',
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'mine',
        component: () => import('@/views/mine/index'),
        meta: { title: 'Mine' }
      }
    ]
  },

  {
    path: '/post',
    name: 'Post',
    component: () => import('@/views/post/index'),
    meta: { title: 'Post' }
  },

  {
    path: '/questionnaire',
    name: 'Questionnaire',
    component: () => import('@/views/questionnaire/index'),
    meta: { title: 'Questionnaire' }
  },

  {
    path: '/check',
    name: 'Check',
    component: () => import('@/views/check/index'),
    meta: { title: 'Check' }
  },

  { path: '*', redirect: '/404', hidden: true }
]

export default new Router({
  // mode: 'history', //后端支持可开
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRouterMap
})
