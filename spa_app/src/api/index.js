import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:8000'

const api = {
  getSeasones () {
    return new Promise((resolve) => {
      axios.get(`/api/v1/seasones/`)
        .then(response => {
          resolve(response.data)
        })
    })
  },
  getSeason (slug) {
    return new Promise((resolve) => {
      axios.get(`/api/v1/seasones/${slug}/`)
        .then(response => {
          resolve(response.data)
        })
    })
  }
}

export default api
