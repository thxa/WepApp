import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1'

const api = {
  getSeasones () {
    return new Promise((resolve, reject) => {
      axios.get(`/api/v1/seasones/`)
        .then(response => {
          resolve(response.data)
        })
        .cache(error => {
          reject(error.data)
        })
    })
  },
  getSeason (slug) {
    return new Promise((resolve, reject) => {
      axios.get(`/api/v1/seasones/${slug}/`)
        .then(response => {
          resolve(response.data)
        })
        .cache(error => {
          reject(error.data)
        })
    })
  },
  postSeason (season) {
    return new Promise((resolve, reject) => {
      axios.post(`/api/v1/seasones/`, season)
        .then(response => {
          resolve(response.data)
        })
        .catch(error => {
          reject(error.data)
        })
    })
  },
  putSeason (slug, season) {
    return new Promise((resolve, reject) => {
      axios.put(`/api/v1/seasones/${slug}/`, season)
        .then(response => {
          resolve(response.data)
        })
        .catch(error => {
          reject(error.data)
        })
    })
  },
  patchSeason (slug, season) {
    return new Promise((resolve, reject) => {
      axios.patch(`/api/v1/seasones/${slug}/`, season)
        .then(response => {
          resolve(response.data)
        })
        .catch(error => {
          reject(error.data)
        })
    })
  },
  deleteSeason (slug) {
    return new Promise((resolve, reject) => {
      axios.delete(`/api/v1/seasones/${slug}/`)
        .then(response => {
          resolve(response.data)
        })
        .catch(error => {
          reject(error.data)
        })
    })
  },
  getVideo (slug) {
    return new Promise((resolve, reject) => {
      axios.get(`/api/v1/videos/${slug}/`)
        .then(response => {
          resolve(response.data)
        })
        .then(error => {
          reject(error.data)
        })
    })
  },
  postVideo (video) {
    return new Promise((resolve, reject) => {
      axios.post(`/api/v1/videos/`, video)
        .then(response => {
          resolve(response.data)
        })
        .cache(error => {
          reject(error.data)
        })
    })
  },
  putVideo (slug, video) {
    return new Promise((resolve, reject) => {
      axios.put(`/api/v1/videos/${slug}/`, video)
        .then(response => {
          resolve(response.data)
        })
        .cache(error => {
          reject(error.data)
        })
    })
  },
  patchVideo (slug, video) {
    return new Promise((resolve, reject) => {
      axios.patch(`/api/v1/videos/${slug}/`)
        .then(response => {
          resolve(response.data)
        })
        .cache(error => {
          reject(error.data)
        })
    })
  },
  deleteVideo (slug) {
    return new Promise((resolve, reject) => {
      axios.delete(`/api/v1/videos/${slug}/`)
        .then(response => {
          resolve(response.data)
        })
        .cache(error => {
          reject(error.data)
        })
    })
  },
  getVideos () {
    return new Promise((resolve) => {
      axios.get(`/api/v1/videos/`)
        .then(response => {
          resolve(response.data)
        })
    })
  }
}

export default api
