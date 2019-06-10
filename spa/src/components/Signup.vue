<template>
    <div v-if="!isAuthentcated">
      <div class="field">
        <p class="control has-icons-left has-icons-right">
          <input class="input" v-model="user.username" type="text" placeholder="username">
          <span class="icon is-small is-left">
            <i class="fas fa-user"></i>
          </span>
          <span class="icon is-small is-right">
            <i class="fas fa-check"></i>
          </span>
        </p>
      </div>
      <div class="field">
        <p class="control has-icons-left has-icons-right">
          <input class="input" v-model="user.email" type="text" placeholder="email">
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
          <input class="input" v-model="user.password" type="password" placeholder="Password">
          <span class="icon is-small is-left">
            <i class="fas fa-lock"></i>
          </span>
        </p>
      </div>
      <div class="field">
        <p class="control">
          <button v-on:click="signUp()" class="button is-success">
            Sign Up
          </button>
        </p>
      </div>

      <div v-if="coreect || error" class="container">
        <div v-if="coreect.username" class="notification is-success">
          {{ coreect.username }}
          {{ coreect.email }}
        </div>

        <div v-if="!error" class="notification is-danger">
          "plase change your username maybe already exiet"
        </div>

      </div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  computed: {
    ...mapGetters(['isAuthentcated']),
    ...mapGetters('signUpModule', ['user', 'coreect', 'error'])
  },
  methods: {
    signUp () {
      this.$store.dispatch('signUpModule/signUp', this.user)
        .then(() => {
          this.user.username = ''
          this.user.password = ''
        })
    }
  }
}
</script>

<style>
</style>
