import apiBase from '@/api/apiBase.js'

export default {
  getVideo (slug) {
    return new Promise((resolve, reject) => {
      apiBase.get(`/api/v1/videos/${slug}/`)
        .then(response => {
          resolve(response.data)
        })
        .catch(error => {
          reject(error.data)
        })
    })
  },
  postVideo (video) {
    return new Promise((resolve, reject) => {
      apiBase.post(`/api/v1/videos/`, video)
        .then(response => {
          resolve(response.data)
        })
        .catch(error => {
          reject(error.data)
        })
    })
  },
  putVideo (slug, video) {
    return new Promise((resolve, reject) => {
      apiBase.put(`/api/v1/videos/${slug}/`, video)
        .then(response => {
          resolve(response.data)
        })
        .catch(error => {
          reject(error.data)
        })
    })
  },
  patchVideo (slug, video) {
    return new Promise((resolve, reject) => {
      apiBase.patch(`/api/v1/videos/${slug}/`)
        .then(response => {
          resolve(response.data)
        })
        .catch(error => {
          reject(error.data)
        })
    })
  },
  deleteVideo (slug) {
    return new Promise((resolve, reject) => {
      apiBase.delete(`/api/v1/videos/${slug}/`)
        .then(response => {
          resolve(response.data)
        })
        .catch(error => {
          reject(error.data)
        })
    })
  },
  getVideos () {
    return new Promise((resolve, reject) => {
      apiBase.get(`/api/v1/videos/`)
        .then(response => {
          resolve(response.data)
        })
        .catch(error => {
          reject(error.data)
        })
    })
  }
}