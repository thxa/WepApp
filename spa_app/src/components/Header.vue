<template>
    <header>
      <nav class="navbar">
        <div class="container">
          <div class="navbar-brand">
            <a class="navbar-item">
              <img src="#" alt="Logo">
            </a>
            <span class="navbar-burger burger" data-target="navbarMenuHeroA">
              <span></span>
              <span></span>
              <span></span>
            </span>
          </div>
          <div id="navbarMenuHeroA" class="navbar-menu">
            <div class="navbar-start">
              <div class="navbar-item field has-addons">
                <div class="control">
                  <input class="input is-rounded" v-model="this.searchSeason" type="text" placeholder="Find a Season">
                </div>
                <div class="control">
                  <a class="button is-info">
                    <i class="fas fa-search"></i>
                  </a>
                </div>
              </div>
            </div>
            <div class="navbar-end">
              <router-link class="navbar-item is-tab" to="/" exact>Home</router-link>
              <router-link class="navbar-item is-tab" to="/about/">about</router-link>
              <!-- <router-link class="navbar-item is-tab" :to="{ name: 'category', params: { slug: 'anime' } }">anime</router-link>
              <router-link class="navbar-item is-tab" :to="{ name: 'category', params: { slug: 'movie' } }">movie</router-link> -->
              <router-link class="navbar-item is-tab" to="/videos/">videos</router-link>
              <router-link v-if="isAuthentcated"
                class="navbar-item is-tab"
                to="/season/create/">Create</router-link>

              <router-link class="navbar-item is-tab" to="/signin/">
                  <span v-if="isAuthentcated">Profile</span>
                  <span v-else>sign in</span></router-link>

              <router-link v-if="isAuthentcated === false" class="navbar-item is-tab" to="/signup/">signUp</router-link>
            </div>
          </div>
        </div>
      </nav>
    </header>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'Header',
  computed: {
    ...mapGetters(['isAuthentcated']),
    ...mapGetters('searchModule', ['searchSeason'])
  },
  methods: {
    searchSeason () {
      this.$store.dispatch('searchModule/searchSeason', this.searchSeason)
    }
  }
}
document.addEventListener('DOMContentLoaded', () => {
  // Get all "navbar-burger" elements
  const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0)
  // Check if there are any navbar burgers
  if ($navbarBurgers.length > 0) {
    // Add a click event on each of them
    $navbarBurgers.forEach(el => {
      el.addEventListener('click', () => {
        // Get the target from the "data-target" attribute
        const target = el.dataset.target
        const $target = document.getElementById(target)
        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        el.classList.toggle('is-active')
        $target.classList.toggle('is-active')
      })
    })
  }
})
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
