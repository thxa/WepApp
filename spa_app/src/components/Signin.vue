<template>
  <div>
    <div v-if="this.isAuthentcated" class="has-text-centered content">
      Welcome to your home
      <button  class="button" type="button is-denger" v-on:click="logout">logout</button>
    </div>

    <div v-else>
      <div class="field">
        <p class="control has-icons-left has-icons-right">
          <input class="input" v-model="username" type="text" placeholder="username">
          <span class="icon is-small is-left">
            <i class="fas fa-envelope"></i>
          </span>
          <span class="icon is-small is-right">
            <i class="fas fa-check"></i>
          </span>
        </p>
      </div>
      <div class="field">
        <p class="control has-icons-left">
          <input class="input" v-model="password" type="password" placeholder="Password">
          <span class="icon is-small is-left">
            <i class="fas fa-lock"></i>
          </span>
        </p>
      </div>
      <div class="field">
        <p class="control">
          <button v-on:click="login()" class="button is-success">
            Login
          </button>
        </p>
      </div>
    </div>

  </div>
</template>

<script>
import api from '@/api/index.js'
export default {
  data () {
    return {
      username: '',
      password: '',
      isAuthentcated: true
    }
  },
  methods: {
    login () {
      api.login({'username': this.username, 'password': this.password})
        .then((data) => {
          window.localStorage.setItem('token', data.access)
          window.localStorage.setItem('tokenExpiration', data.refresh)
          this.isAuthentcated = true
          this.username = ''
          this.password = ''
          console.log(data)
        })
        .catch(() => window.alert('Could not login!'))
    },
    logout () {
      // window.localStorage.setItem('token', null)
      // window.localStorage.setItem('tokenExpiration', null)
      window.localStorage.removeItem('token')
      window.localStorage.removeItem('tokenExpiration')
      this.isAuthentcated = false
    }
  },
  created () {
    let expiration = window.localStorage.getItem('tokenExpiration')
    // var unixTimestamp = new Date().getTime() / 1000
    if (expiration !== null) {
      // && parseInt(expiration) - unixTimestamp > 0
      this.isAuthentcated = true
    }
  }
}
</script>

<style>
</style>
