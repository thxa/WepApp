import api from '@/api/index.js'

const state = {
  seasones: [],
  season: {},
  newSeason: {
    'name': '',
    'photo_url': '',
    'number_of_episodes': 1,
    'category': [],
    'episodes': []
  }
}

const getters = {
  seasones: state => state.seasones,
  season: state => state.season,
  newSeason: state => state.newSeason
}

const actions = {
  loadSeasones (context) {
    api.getSeasones().then(data => {
      context.commit('loadSeasones', { seasones: data })
    })
  },
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
  loadSeasones (state, data) {
    state.seasones = data.seasones
  },
  loadSeason (state, data) {
    state.season = data.season
  },
  createSeason (state, data) {
    // state.season = data.season
    window.alert('success')
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
