import api from '@/api/index.js'

const state = {
  user: {
    username: '',
    email: '',
    password: ''
  },
  coreect: {},
  error: {}
}

const getters = {
  user: state => state.user,
  coreect: state => state.coreect,
  error: state => state.error
}
const actions = {
  signUp (context, user) {
    api.signUp(user)
      .then(data => {
        context.commit('signUp', { user: data })
      })
      .catch(data => {
        context.commit('signUpFailed', { error: data })
      })
  }
}

const mutations = {
  signUp (state, data) {
    // state.user = user
    state.coreect = data.user
  },
  signUpFailed (state, data) {
    state.error = data.error
    // window.alert(data.error)
    // state.error = data.error
    // {
    //   username: ['This field may not be blank.'],
    //   password: ['This field may not be blank.']
    // }
    // window.alert(`cannot signup ${error.data}`)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
