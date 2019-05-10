<template>
  <div class="container main section">
    <div class="title has-text-centered">
    {{season.name}}
    </div>
    <div class="">
      <div class="button">
        <i class="far fa-edit"></i>
      </div>
      <button v-on:click="deleteSeason()" class="button">
        <i class="fas fa-trash"></i>
      </button>
    </div>
    <div class="card img">
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
          <div class="column is-one-quarter" v-for="episode in season.episodes"
          v-bind:key="episode.created">
          <div class="card">
            <div class="">
              {{episode.name}}
            </div>
            <router-link :to="{ name: 'Video', params: {slug: episode.slug} }" class="img">
              <img :src="episode.photo_url" alt="">
            </router-link>
            <button class="button">
              <i class="far fa-edit"></i>
            </button>
            <button v-on:click="deleteVideo(episode.slug)" class="button">
              <i class="fas fa-trash"></i>
            </button>
          </div>
        </div>
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
    },
    updateSeason () {
      api.putSeason(this.slug, this.season)
        .then(data => {
          this.season = data
          console.log(data)
        })
        .catch(error => {
          console.log(error)
        })
    },
    deleteSeason () {
      api.deleteSeason(this.slug)
        .then(data => {
          console.log(data)
        })
        .catch(error => {
          console.log(error)
        })
    },
    updateVideo (slug, video) {
      api.putVideo(slug, video)
        .then(data => {
          video = data
          console.log(data)
        })
        .catch(error => {
          console.log(error)
        })
    },
    deleteVideo (slug) {
      api.deleteVideo(slug)
        .then(data => {
          console.log(data)
        })
        .catch(error => {
          console.log(error)
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
