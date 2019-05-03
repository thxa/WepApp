<template>
  <div class="container main section">
    <div class="title has-text-centered">
    {{season.name}}
    </div>
    <div class="img">
      <img :src="season.photo_url">
    </div>
    <div class="">
            created: {{season.created}}<br>
            category:
        <div class="" v-for="category in season.category"
        v-bind:key="category.id">
        {{category}}
        </div>
      <div class="">
        <div class="title has-text-centered">
          episodes
          <hr>
        </div>
        <div class="columns">
          <router-link class="column is-one-quarter" v-for="episod in season.episodes"
          :to="{ name: 'Video', params: {slug: episod.slug} }"
          v-bind:key="episod.created">
          <div class="card">
            <div class="">
              {{episod.name}}
            </div>
            <div class="">
              <img :src="episod.photo_url" alt="">
            </div>
          </div>
        </router-link>
      </div>

      </div>
    </div>
  </div>
</template>

<script>
import api from '@/api/index.js'
export default {
  data () {
    return {
      slug: this.$route.params.slug,
      season: {}
    }
  },
  methods: {
    loadSeason () {
      api.getSeason(this.slug)
        .then(data => {
          console.log(data)
          this.season = data
        })
    }
  },
  watch: {
    '$route' (to, from) {
      this.slug = to.params.slug
      this.loadSeason()
      console.log(this.$route.query.page)
    }
  },
  created () {
    this.loadSeason()
  }
}
</script>
<style>
</style>
