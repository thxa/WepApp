<template>
  <div>
    <section class="hero is-medium">
      <div class="hero-head is-warning">
          <div class="title has-text-centered">
            Videos
          </div>
        </div>

      <div class="hero-body">
        <div class="container has-text-centered">
            <div v-if="videos"
            class="columns is-desktop">
            <videos></videos>
          </div>
          <div v-else class="notification is-warning">
              Nothing
          </div>
        </div>
      </div>
  </section>

  <section class="hero  is-medium">
    <div class="hero-head ">
        <div class="title has-text-centered">
          sesone
        </div>
      </div>

    <div class="hero-body">
      <div class="container has-text-centered">
        <div class="columns is-desktop">
            <router-link
            :to="{ name: 'Season', params: { slug: season.slug} }"
            class="column is-one-quarter"
            v-for="season in seasones"
            v-bind:key="season.id">
            <box :link="season.link">
              <h3 slot="name">{{season.name}}</h3>
              <img slot="photo_url" :src="season.photo_url">
            </box>
          </router-link>
        </div>
      </div>
    </div>
  </section>
  </div>
</template>

<script>
import Box from '@/components/Box.vue'
import Videos from '@/components/Videos.vue'
import { mapGetters } from 'vuex'
export default {
  name: 'Index',
  components: {
    'box': Box,
    'videos': Videos
  },
  computed: {
    ...mapGetters('seasonModule', ['seasones']),
    ...mapGetters('videoModule', ['videos'])
  },
  methods: {
    loadSeasones () {
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
      this.$store.dispatch('seasonModule/loadSeasones')
    }
    // loadVideos () {
    //   this.$store.dispatch('videosModule/loadVideos')
    // }
  },
  watch: {
    '$route' (to, from) {
      // this.slug = to.params.slug
      this.loadSeasones()
      // console.log(this.$route.query.page)
    }
  },
  created () {
    // this.loadVideos()
    this.loadSeasones()
  }
}
</script>

<style>
.columns {
  flex-wrap: wrap;
}
.column {
  /* margin: 1%; */
  /* background-color: blue; */
  /* border: solid 1px black; */

}
</style>
