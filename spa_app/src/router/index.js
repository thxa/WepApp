import Vue from 'vue'
import Router from 'vue-router'

import Index from '@/components/Index'
import About from '@/components/About'
import NotFound from '@/components/NotFound'
import SeasonDeteiles from '@/components/SeasonDeteiles'
// const Index = () => System.import('@/components/Index.vue')
// const About = () => System.import('@/components/About.vue')
// const NotFound = () => System.import('@/components/NotFound.vue')

Vue.use(Router)

export default new Router({
  mode: 'history',
  linkActiveClass: 'is-active',
  scrollBehavior: (to, from, savedPosition) => ({ y: 0 }),
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index
    },
    {
      path: '/about/',
      name: 'About',
      component: About
    },
    {
      path: '*',
      // redirect: '/',
      name: 'NotFound',
      component: NotFound
    },
    {
      path: '/category/:slug/',
      name: 'category',
      component: Index
    },
    {
      path: '/seasones/:slug/',
      name: 'Season',
      component: SeasonDeteiles
    }
  ]
})
