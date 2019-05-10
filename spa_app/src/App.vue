<template>
    <section class="hero is-danger is-medium">
      <Header></Header>
      <div class="hero-body">
        <div class="container">
          <router-view/>
        </div>
      </div>
      <Footer></Footer>
    </section>
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
