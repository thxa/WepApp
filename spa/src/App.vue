<template>
  <div>
    <Header></Header>

    <main class="main">
      <div class="container">
        <router-view/>
      </div>
    </main>

    <Footer></Footer>
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

<style lang="sass">
@import 'bulma'

</style>
