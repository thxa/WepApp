import api from '@/api/index.js'

const state = {
  videos: [],
  video: {},
  episode: {
    'name': '',
    'photo_url': '',
    'video_url': '',
    'season': ''
  }
}

const getters = {
  videos: state => state.videos,
  video: state => state.video,
  episode: state => state.episode
}

const actions = {
  loadVideos (context) {
    api.getVideos()
      .then(data => {
        context.commit('loadVideos', { videos: data })
      })
  },
  loadVideo (context, slug) {
    api.getVideo(slug)
      .then(data => {
        context.commit('loadVideo', { video: data })
      })
  },
  createVideo (context, video) {
    api.postVideo(video)
      .then(data => {
        context.commit('createVideo', { episode: data })
      })
      .catch(error => { window.alert(`error: ${error.status}`) })
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
  loadVideos (state, data) {
    state.videos = data.videos
  },
  loadVideo (state, data) {
    state.video = data.video
  },
  createVideo (state, data) {
    // state.episode = data.episode
    window.alert('success')
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
