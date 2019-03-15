<template>

<div class="">
  <div class="hero-head">
      <nav class="navbar">
        <div class="container">
          <div class="navbar-brand">
            <a class="navbar-item">
              <img src="https://bulma.io/images/bulma-type-white.png" alt="Logo">
            </a>
            <span class="navbar-burger burger" data-target="navbarMenuHeroA">
              <span></span>
              <span></span>
              <span></span>
            </span>
          </div>
          <div id="navbarMenuHeroA" class="navbar-menu">
            <div class="navbar-end">
              <router-link class="navbar-item is-tab" to="/" exact>Home</router-link>
              <router-link class="navbar-item is-tab" to="/about/">about</router-link>
              <router-link class="navbar-item is-tab" :to="{ name: 'category', params: { slug: 'anime' } }">anime</router-link>
              <router-link class="navbar-item is-tab" :to="{ name: 'category', params: { slug: 'movie' } }">movie</router-link>
              <router-link class="navbar-item is-tab" to="/videos/">videos</router-link>
              <router-link class="navbar-item is-tab" to="/season/create/">Create</router-link>
            </div>
          </div>
        </div>
      </nav>
    </div>
</div>
</template>

<script>
export default {
  name: 'Header',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
