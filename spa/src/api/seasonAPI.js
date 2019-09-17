import apiBase from '@/api/apiBase.js'

export default {
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
  }
}