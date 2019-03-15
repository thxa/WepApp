<template>
  <header>
    <nav class="navbar has-shadow">
      <div class="navbar-brand">
        <a class="navbar-item" href="#">
          <img src="logo.png" alt="Webapp">
        </a>
      </div>

      <div class="navbar-burger burger">
        <span></span>
        <span></span>
        <span></span>
      </div>

      <div class="navbar-menu">
        <div class="navbar-start">

          <router-link class="navbar-item is-tab" to="/" exact>Home</router-link>
          <router-link class="navbar-item is-tab" to="/about/">about</router-link>
          <router-link class="navbar-item is-tab" :to="{ name: 'category', params: { slug: 'anime' } }">anime</router-link>
          <router-link class="navbar-item is-tab" :to="{ name: 'category', params: { slug: 'movie' } }">movie</router-link>
          <div class="navbar-dropdown">
            <div id="categories" class="navbar-item">
              categories
            </div>
          </div>
        </div>

        <div class="navbar-end">
            <router-link class="navbar-item is-tab" to="/season/create/">Create</router-link>
        </div>
      </div>
    </nav>
  </header>
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
