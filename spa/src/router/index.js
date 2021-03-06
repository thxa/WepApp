import Vue from 'vue'
import Router from 'vue-router'

// import Index from '@/views/Index'
// import About from '@/components/About'
// import NotFound from '@/components/NotFound'
// import SeasonDeteiles from '@/components/SeasonDeteiles'
// import Create from '@/components/Create'
// import Video from '@/components/Video'
// import Videos from '@/components/Videos'
// import Signin from '@/views/Signin'
// import Signup from '@/views/Signup'

const Index = () => import('@/views/Index.vue')
const About = () => import('@/components/About.vue')
const NotFound = () => import('@/components/NotFound.vue')
const SeasonDeteiles = () => import('@/components/SeasonDeteiles.vue')
const Create = () => import('@/components/Create.vue')
const Video = () => import('@/components/Video.vue')
const Videos = import('@/components/Videos.vue')
const Signin = () => import('@/views/Signin.vue')
const Signup = () => import('@/views/Signup.vue')

Vue.use(Router)

export default new Router({
//  mode: 'history',
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
