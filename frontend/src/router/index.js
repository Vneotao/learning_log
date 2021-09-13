import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/pages/index'
import Topics from '@/pages/topics'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: Index
    },
    {
      path: '/topics',
      name: 'topics',
      component: Topics
    }
  ]
})
