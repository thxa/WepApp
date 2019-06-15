import api from '@/api/index.js'

const state = {
  seasonName: '',
  seasonesResult: []
}

const getters = {
  seasonName: state => state.seasonName,
  seasonesResult: state => state.seasonesResult
}

const actions = {
  searchSeason (context, seasonName) {
    api.searchSeason(seasonName)
      .then(data => {
        context.commit('searchSeason', { seasonesResult: data })
      })
  }
}

const mutations = {
  searchSeason (state, data) {
    state.seasonesResult = data.seasonesResult
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
