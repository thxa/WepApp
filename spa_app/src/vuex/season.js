import api from '@/api/index.js'

const state = {
  season: {},
  newSeason: {
    'name': '',
    'photo_url': '',
    'number_of_episodes': 1
  }
}

const getters = {
  season: state => state.season,
  newSeason: state => state.newSeason
}

const actions = {
  loadSeason (context, slug) {
    api.getSeason(slug)
      .then(data => {
        context.commit('loadSeason', { season: data })
      })
      .catch(data => { window.alert(data) })
  },
  createSeason (context, season) {
    api.postSeason(season)
      .then(data => {
        context.commit('createSeason', { season: data })
      })
  },
  updateSeason (context, slug, season) {
    api.putSeason(slug, season)
      .then(data => {
        context.commit('updateSeason', { season: data })
      })
  },
  patchSeason (context, slug, season) {
    api.putSeason(slug, season)
      .then(data => {
        context.commit('patchSeason', { season: data })
      })
  },
  deleteSeason (context, slug) {
    api.deleteSeason(slug)
      .then(data => {
        context.commit('deleteSeason', { season: data })
      })
      .catch(error => {
        window.alert(error)
      })
  }
}

const mutations = {
  loadSeason (state, data) {
    state.season = data.season
  },
  createSeason (state, data) {
    state.season = data.season
  },
  updateSeason (state, data) {
    state.season = data.season
  },
  patchSeason (state, data) {
    state.season = data.season
  },
  deleteSeason (state, data) {
    state.season = data.season
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
