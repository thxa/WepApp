import Vue from 'vue'
import Vuex from 'vuex'
import api from '@/api/index.js'
import seasonModule from './modules/season.js'
import videoModule from './modules/video.js'
import searchModule from './modules/search.js'
import signUpModule from './modules/signup.js'

Vue.use(Vuex)

const state = {
  isAuthentcated: false
}

const store = new Vuex.Store({
  modules: {
    seasonModule,
    videoModule,
    searchModule,
    signUpModule
  },
  state,
  getters: {
    isAuthentcated: (state) => {
      return state.isAuthentcated
    }
  },
  actions: {
    logout (context) {
      context.commit('logout')
    },
    login (context, credentials) {
      return new Promise((resolve) => {
        api.login(credentials)
          .then((data) => {
            context.commit('login', data)
            resolve()
          })
          .catch(() => window.alert('Could not login!'))
      })
    }
  },
  mutations: {
    logout (state) {
      if (typeof window !== 'undefined') {
        window.localStorage.removeItem('token')
        window.localStorage.removeItem('tokenExpiration')
      }
      state.isAuthentcated = false
    },
    login (state, token) {
      if (typeof window !== 'undefined') {
        window.localStorage.setItem('token', token.token)
        // window.localStorage.setItem('token', token.access)
        // window.localStorage.setItem('tokenExpiration', token.refresh)
      }
      state.isAuthentcated = true
    }
  }
})

if (typeof window !== 'undefined') {
  document.addEventListener('DOMContentLoaded', (event) => {
    let token = window.localStorage.getItem('token')
    // let expiration = window.localStorage.getItem('tokenExpiration')
    // var unixTimestamp = new Date().getTime() / 1000
    if (token !== null) {
      // && parseInt(expiration) - unixTimestamp > 0
      store.state.isAuthentcated = true
    }
  })
}

export default store
