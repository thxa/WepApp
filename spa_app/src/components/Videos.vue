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
import api from '@/api/index.js'

export default {
  name: 'Videos',
  components: {
    'box': Box
  },
  data () {
    return {
      // slug: this.$route.params.slug,
      videos: []
    }
  },
  methods: {
    loadVideos () {
      // if (this.slug === 'movie') {
      //   this.seasones = this.movie
      // } else {
      //   this.seasones = this.anime
      // }

      // if (this.slug === 'season') {
      //   this.seasones = this.videos
      // } else {
      //   this.seasones = this.season
      // }
      api.getVideos()
        .then(data => {
          console.log(data)
          this.videos = data
        })
    }
  },
  watch: {
    '$route' (to, from) {
      // this.slug = to.params.slug
      // this.loadSeasones()
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
