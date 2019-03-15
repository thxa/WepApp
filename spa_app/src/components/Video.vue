<template>
  <div class="">
    <div class="title">
      {{video.name}}
    </div>
    <div class="">
      <iframe :src="video.url" width="640" height="360" frameborder="0" allowfullscreen></iframe>
    </div>
  </div>
</template>

<script>
import api from '@/api/index.js'
export default {
  data () {
    return {
      slug: this.$route.params.slug,
      video: {}
    }
  },
  methods: {
    loadVideo () {
      api.getVideo(this.slug)
        .then(data => {
          console.log(data)
          this.video = data
        })
    }
  },
  watch: {
    '$route' (to, from) {
      this.slug = to.params.slug
      this.loadVideo()
      console.log(this.$route.query.page)
    }
  },
  created () {
    this.loadVideo()
  }
}
</script>

<style>
</style>
