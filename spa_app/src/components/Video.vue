<template>
  <div class="has-text-centered">
    <div class="title">
      {{video.name}}
    </div>
    <div class="">
      <iframe :src="video.url" width="640" height="360" frameborder="0" allowfullscreen></iframe>
    </div>
    <div class="">
      <nav class="pagination" role="navigation" aria-label="pagination">
        <a class="pagination-previous" title="This is the first page" disabled>Previous</a>
        <a class="pagination-next">Next page</a>
    <ul class="pagination-list">
      <li>
        <a class="pagination-link is-current" aria-label="Page 1" aria-current="page">1</a>
      </li>
      <li>
        <a class="pagination-link" aria-label="Goto page 2">2</a>
      </li>
      <li>
        <a class="pagination-link" aria-label="Goto page 3">3</a>
      </li>
    </ul>
</nav>
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
