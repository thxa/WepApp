<template>
  <div>
    <section class="hero is-primary is-medium">
      <Header></Header>
    <div class="hero-body">
      <div class="container has-text-centered">
        <router-view/>
    </div>
  </div>
      <Footer></Footer>
    </section>
  </div>
</template>

<script>
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'

export default {
  name: 'App',
  components: {
    Header,
    Footer
  }
}
</script>

<style>
</style>
