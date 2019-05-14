import api from '@/api/index.js'

const state = {
  videos: []
}

const getters = {
  videos: state => state.videos
}

const actions = {
  loadVideos (context) {
    api.getVideos()
      .then(data => {
        context.commit('loadVideos', { videos: data })
      })
  }
}

const mutations = {
  loadVideos (state, data) {
    state.videos = data.videos
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
