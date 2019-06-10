<template>
  <div class="container has-text-centered">
    <div class="title">
      {{video.name}}
    </div>
    <div class="is-fullwidth">
      <!-- <iframe :src="video.video_url" allowfullscreen="true" allowscriptaccess="always" ></iframe> -->
      <iframe  :src="video.video_url" width="640" height="360" frameborder="0" allowfullscreen></iframe>
    </div>
    <div class="">
      <nav class="pagination" role="navigation" aria-label="pagination">
        <button v-on:click="previousVideo()" class="pagination-previous" title="This is the first page" disabled>Previous</button>
        <button v-on:click="nextVideo()" class="pagination-next">Next</button>

        <ul class="pagination-list">
          <li>
            <router-link to="#" class="pagination-link is-current" aria-label="1" aria-current="page">1</router-link>
          </li>
          <li>
            <router-link to="#" class="pagination-link" aria-label="Page 2" aria-current="page">2</router-link>
          </li>
        </ul>
      </nav>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  computed: {
    ...mapGetters('videoModule', ['video'])
  },
  methods: {
    loadVideo () {
      this.slug = this.$route.params.slug
      this.$store.dispatch('videoModule/loadVideo', this.slug)
    },
    updateVideo () {
      this.$store.dispatch('videoModule/upadteVideo', this.slug, this.video)
    },
    deleteVideo () {
      this.$store.dispatch('videoModule/deleteVideo', this.slug)
    },
    nextVideo () {
      console.log('next Video')
    },
    previousVideo () {
      console.log('previous Video')
    }
  },
  watch: {
    '$route' (to, from) {
      // this.slug = to.params.slug
      this.loadVideo()
      // console.log(this.$route.query.page)
    }
  },
  created () {
    this.loadVideo()
  }
}
</script>

<style>
</style>
