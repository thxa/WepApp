import Vue from 'vue'
import Router from 'vue-router'

import Index from '@/views/Index'
import About from '@/components/About'
import NotFound from '@/components/NotFound'
import SeasonDeteiles from '@/components/SeasonDeteiles'
import Create from '@/components/Create'
import Video from '@/components/Video'
import Videos from '@/components/Videos'
import Signin from '@/views/Signin'
import Signup from '@/views/Signup'

// const Index = () => System.import('@/views/Index.vue')
// const About = () => System.import('@/views/About.vue')
// const NotFound = () => System.import('@/views/NotFound.vue')
// const SeasonDeteiles = () => System.import('@/components/SeasonDeteiles.vue')
// const  Create = () => System.import('@/components/Create.vue)'
// const Video = () => System.import('@/components/Video.vue')
// const Videos = System.import('@/components/Videos.vue')
// const Signin = () => System.import('@/views/Signin.vue')
// const Signup = () => System.import('@/views/Signup.vue')

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
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
      path: '/signin/',
      name: 'Signin',
      component: Signin
    },
    {
      path: '/signup/',
      name: 'Signup',
      component: Signup
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
    },
    {
      path: '/season/create/',
      name: 'Create',
      component: Create
    },
    {
      path: '/video/:slug/',
      name: 'Video',
      component: Video
    },
    {
      path: '/videos/',
      name: 'Videos',
      component: Videos
    }
  ]
})
