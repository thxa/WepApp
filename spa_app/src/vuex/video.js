import api from '@/api/index.js'

const state = {
  video: {},
  episode: {
    'name': '',
    'photo_url': '',
    'url': '',
    'season': ''
  }
}

const getters = {
  video: state => state.video,
  episode: state => state.episode
}

const actions = {
  loadVideo (context, slug) {
    api.getVideo(slug)
      .then(data => {
        context.commit('loadVideo', { video: data })
      })
  },
  createVideo (context, video) {
    api.postVideo(slug, video)
      .then(data => {
        context.commit('createVideo', { episode: data })
      })
      .catch(error => {
        console.log(error)
      })
  },
  updateVideo (context, slug, video) {
    api.putVideo(slug, video)
      .then(data => {
        context.commit('updateVideo', { video: data })
      })
      .catch(error => {
        console.log(error)
      })
  },
  patchVideo (context, slug, video) {
    api.patchVideo(slug, video)
      .then(data => {
        context.commit('patchVideo', { video: data })
      })
      .catch(error => {
        console.log(error)
      })
  },
  deleteVideo (context, slug) {
    api.deleteVideo(slug)
      .then(data => {
        context.commit('deleteVideo', { video: data })
      })
      .catch(error => {
        console.log(error)
      })
  }
}

const mutations = {
  loadVideo (state, data) {
    state.video = data.video
  },
  createVideo (state, data) {
    state.episode = data.episode
  },
  updateVideo (state, data) {
    state.video = data.video
  },
  patchVideo (state, data) {
    state.video = data.video
  },
  deleteVideo (state, data) {
    state.video = data.video
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
