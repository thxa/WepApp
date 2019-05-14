import api from '@/api/index.js'

const state = {
  seasones: []
}

const getters = {
  seasones: state => state.seasones
}
const actions = {
  updateSeasones (context) {
    api.getSeasones().then(data => {
      context.commit('updateSeasones', { seasones: data })
    })
  }
}

const mutations = {
  updateSeasones (state, seasones) {
    state.seasones = seasones.seasones
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
