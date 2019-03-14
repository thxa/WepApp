<template>
  <div>
        <!-- <main>
        </main> -->
    <!--
    <div class="block">
      <div class="title"> name</div>

      <div class="img">
        <img src="#" alt="photo">
      </div>

      <div class="video"> url_video</div>

    </div> -->
    <Header></Header>
    <router-view/>
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

<style>
</style>
