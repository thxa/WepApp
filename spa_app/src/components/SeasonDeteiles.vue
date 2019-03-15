<template>
  <div class="container main section">
    <div class="title is-centerd">
      name: {{season.name}}
    </div>
    <div class="">
      <img :src="season.photo_url">
    </div>
    <div class="">
            created: {{season.created}}<br>
            slug: {{season.slug}} <br>
            category: {{season.category}} <br>
      <div class="columns">
        <div class="column" v-for="category in season.category"
        v-bind:key="category.id">
        {{category}}
        </div>
      </div>
      episodes: {{season.episodes}}
      <div class="columns">
        <router-link class="column" v-for="episod in season.episodes"
        :to="{ name: 'Video', params: {slug: episod} }"
        v-bind:key="episod">
        {{episod}}
      </router-link>
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
