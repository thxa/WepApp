<template>
  <div class="">
    <div class="columns is-desktop">
      <router-link class="column  is-one-quarter"
      v-for="video in videos"
      :to="{ name: 'Video', params: { slug: video.slug} }"
      v-bind:key="video.id">
        <box :link="video.link">
          <h3 slot="name">{{video.name}}</h3>
          <img slot="photo_url" :src="video.photo_url">
        </box>
      </router-link>
    </div>
  </div>
</template>

<script>
import Box from '@/components/Box.vue'
import { mapGetters } from 'vuex'

export default {
  name: 'Videos',
  components: {
    'box': Box
  },
  computed: {
    ...mapGetters('videosModule', ['videos'])
  },
  methods: {
    loadVideos () {
      this.$store.dispatch('videosModule/loadVideos')
    }
  },
  watch: {
    '$route' (to, from) {
      // this.slug = to.params.slug
      this.loadVideos()
      // console.log(this.$route.query.page)
    }
  },
  created () {
    this.loadVideos()
  }
}
</script>

<style>
</style>
