import api from '@/api/index.js'

const state = {
  searchSeason: []
}

const getters = {
  searchSeason: state => state.searchSeason
}

const actions = {
  search (context, nameSeason) {
    api.FilterSeason(nameSeason)
      .then(data => {
        context.commit('searchSeason', { searchSeason: data })
      })
  }
}

const mutations = {
  searchSeason (state, data) {
    state.searchSeason = data.searchSeason
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
