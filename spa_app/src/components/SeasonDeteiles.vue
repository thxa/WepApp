<template>
  <div class="container main section">
    <div class="title has-text-centered">
    {{season.name}}
    </div>
    <div v-if="isAuthentcated" class="">
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
              <i v-if="isAuthentcated" class="far fa-edit"></i>
            </button>
            <button v-if="isAuthentcated" v-on:click="deleteVideo(episode.slug)" class="button">
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
import { mapGetters } from 'vuex'
export default {
  computed: {
    ...mapGetters(['isAuthentcated']),
    ...mapGetters('seasonModule', ['season']),
    ...mapGetters('videoModule', ['video'])
  },
  methods: {
    loadSeason () {
      this.slug = this.$route.params.slug
      this.$store.dispatch('seasonModule/loadSeason', this.slug)
    },
    updateSeason () {
      this.$store.dispatch('seasonModule/updateSeason', this.slug, this.season)
    },
    deleteSeason () {
      this.$store.dispatch('seasonModule/deleteSeason', this.slug)
    },
    updateVideo (slug, video) {
      this.$store.dispatch('videoModule/upadteVideo', slug)
    },
    deleteVideo (slug) {
      this.$store.dispatch('videoModule/deleteVideo', slug)
    }
  },
  watch: {
    '$route' (to, from) {
      // this.slug = to.params.slug
      this.loadSeason()
      // console.log(this.$route.query.page)
    }
  },
  created () {
    this.loadSeason()
  }
}
</script>
<style>
</style>
