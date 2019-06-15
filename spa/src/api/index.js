import apiBase from '@/api/apiBase.js'

// axios.defaults.baseURL = 'http://0.0.0.0:8000'

apiBase.interceptors.request.use((config) => {
  if (typeof window === 'undefined') {
    return config
  }
  const token = window.localStorage.getItem('token')
  if (token) {
    // config.headers.Authorization = `Bearer ${token}` // this is JWT
    config.headers.Authorization = `Token ${token}` // this is Token
  }

  return config
})

const api = {
  getSeasones () {
    return new Promise((resolve, reject) => {
      apiBase.get(`/api/v1/seasones/`)
        .then(response => {
          resolve(response.data)
        })
        .catch(error => {
          reject(error.data)
        })
    })
  },
  getSeason (slug) {
    return new Promise((resolve, reject) => {
      apiBase.get(`/api/v1/seasones/${slug}/`)
        .then(response => {
          resolve(response.data)
        })
        .catch(error => {
          reject(error.data)
        })
    })
  },
  postSeason (season) {
    return new Promise((resolve, reject) => {
      apiBase.post(`/api/v1/seasones/`, season)
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
      apiBase.put(`/api/v1/seasones/${slug}/`, season)
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
      apiBase.patch(`/api/v1/seasones/${slug}/`, season)
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
      apiBase.delete(`/api/v1/seasones/${slug}/`)
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
  },
  login (credentials) {
    return new Promise((resolve, reject) => {
      apiBase.post('/api/auth/login/', credentials)
        .then(response => {
          resolve(response.data)
        })
        .catch(response => {
          reject(response.status)
        })
    })
  },
  signUp (credentials) {
    return new Promise((resolve, reject) => {
      apiBase.post('/api/auth/signup/', credentials)
        .then(response => {
          resolve(response.data)
        })
        .catch(error => {
          reject(error.status)
        })
    })
  },
  searchSeason (seasonName) {
    return new Promise((resolve, reject) => {
      apiBase.get(`/api/v1/seasones/?search=${seasonName}`)
        .then(response => {
          resolve(response.data)
        })
        .catch(response => {
          reject(response.status)
        })
    })
  }
}
export default api
