<template>
  <div class="container">
    <div v-if="this.isAuthentcated" class="has-text-centered content">
      Welcome to your home
      <button  class="button is-danger" type="button" v-on:click="logout">logout</button>
    </div>

    <div v-else>
      <!-- username field -->
      <div class="field">
        <p class="control has-icons-left has-icons-right">
          <input class="input" v-model="username" type="text" placeholder="username">
          <span class="icon is-small is-left">
            <i class="fas fa-user"></i>
          </span>
          <span class="icon is-small is-right">
            <i class="fas fa-check"></i>
          </span>
        </p>
      </div>

      <!-- password field -->
      <div class="field">
        <p class="control has-icons-left">
          <input class="input" v-model="password" type="password" placeholder="Password">
          <span class="icon is-small is-left">
            <i class="fas fa-lock"></i>
          </span>
        </p>
      </div>

      <!-- Login field -->
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
import { mapGetters, mapActions } from 'vuex'
export default {
  data () {
    return {
      username: '',
      password: ''
    }
  },
  computed: {
    ...mapGetters(['isAuthentcated'])
  },
  methods: {
    ...mapActions({
      logout: 'logout'
    }),
    login () {
      this.$store.dispatch('login', {username: this.username, password: this.password})
        .then(() => {
          this.username = ''
          this.password = ''
        })
    }
  }
}
</script>

<style>
</style>
