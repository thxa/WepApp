<template>
  <div class="container main section">
    <div v-if="isAuthentcated">
      <button class="button">
        <i v-on:click="updateSeason()" class="far fa-edit"></i>
      </button>
      <button v-on:click="deleteSeason()" class="button">
        <i class="fas fa-trash"></i>
      </button>
    </div>
    <!-- photo Season-->
    <div class="media">
      <!-- has-text-right -->
<!-- has-text-left -->
        <div class="media-left">
          <div>
            name: {{season.name}}
          </div>
          <div>
            created: {{season.created}}<br>
          </div>
        <div>
          category:
            <div v-for="category in season.category"
            v-bind:key="category.id">
            {{category}}
            </div>
        </div>
      </div>
      <div class="media-right">
        <img class="image" :src="season.photo_url">
      </div>
    </div>
    <!--  details season -->
    <div>

      <div>
        <!-- episodes -->
        <div class="has-text-6 has-text-centered">
          episodes
        </div>
        <hr>
        <!-- video list -->
        <div class="container">
          <div class="columns">
            <div class="column is-one-quarter" v-for="episode in season.episodes"
            v-bind:key="episode.created">
              <div class="card">
                <router-link :to="{ name: 'Video', params: {slug: episode.slug} }">
                <!-- title -->
                <div class="title">
                  {{episode.name}}
                </div>
                <!-- photo -->
                  <img class="img" :src="episode.photo_url" alt="">

                </router-link>
                <!-- Edit-->
                <button v-if="isAuthentcated" class="button">
                  <i class="far fa-edit"></i>
                </button>

                <!-- Delete -->
                <button v-if="isAuthentcated" v-on:click="deleteVideo(episode.slug)" class="button">
                  <i class="fas fa-trash"></i>
                </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

    <hr>
      <!-- video name -->
      <div class="field">
        <p class="control has-icons-left has-icons-right">
          <input class="input" v-model="episode.name" type="text" placeholder="video name">
          <span class="icon is-small is-left">
          </span>
          <span class="icon is-small is-right">
            <i class="fas fa-check"></i>
          </span>
        </p>
      </div>

      <!-- video photo url -->
      <div class="field">
        <p class="control has-icons-left has-icons-right">
          <input class="input"  v-model="episode.photo_url" type="url" placeholder="photo url">
          <span class="icon is-small is-left">
            <i class="fas fa-image"></i>
          </span>
          <span class="icon is-small is-right">
          </span>
        </p>
      </div>

      <!-- video url -->
      <div class="field">
        <p class="control has-icons-left has-icons-right">
          <input class="input"  v-model="episode.video_url" type="url" placeholder="video url">
          <span class="icon is-small is-left">
            <i class="fas fa-film"></i>
          </span>
          <span class="icon is-small is-right">
          </span>
        </p>
      </div>
      <button class="button is-success" v-on:click="createVideo()">create</button>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  computed: {
    ...mapGetters(['isAuthentcated']),
    ...mapGetters('seasonModule', ['season']),
    ...mapGetters('videoModule', ['episode'])
  },
  methods: {
    loadSeason () {
      this.slug = this.$route.params.slug
      this.$store.dispatch('seasonModule/loadSeason', this.slug)
    },
    updateSeason () {
      // let updated = false
      this.$store.dispatch('seasonModule/updateSeason', this.slug, this.season)
    },
    deleteSeason () {
      this.$store.dispatch('seasonModule/deleteSeason', this.slug)
    },
    createVideo () {
      if (this.episode.name) {
        let seasonId = this.season.url
        this.episode.season = seasonId
        this.$store.dispatch('videoModule/createVideo', this.episode)
        window.reloed()
      } else {
        window.alert('plase write video name')
      }
    },
    updateVideo (slug, video) {
      this.$store.dispatch('videoModule/upadteVideo', slug, video)
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
.columns {
  flex-wrap: wrap;
}
</style>
