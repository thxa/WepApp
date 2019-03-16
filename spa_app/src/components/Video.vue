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
        <router-link to="#" class="pagination-previous" title="This is the first page" disabled>Previous</router-link>
        <router-link to="#" class="pagination-next">Next</router-link>

        <ul class="pagination-list">
          <li>
            <router-link to="#" class="pagination-link is-current" aria-label="Page 1" aria-current="page">1</router-link>
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
