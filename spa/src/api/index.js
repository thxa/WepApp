import apiBase from '@/api/apiBase.js'
import seasonAPI from '@/api/seasonAPI.js'
import videoAPI from '@/api/videoAPI.js'
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
  seasonAPI,
  videoAPI,
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
          reject(error)
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
