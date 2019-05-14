<template>
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
</template>

<script>
import Box from '@/components/Box.vue'
import { mapGetters } from 'vuex'
export default {
  name: 'Index',
  components: {
    'box': Box
  },
  computed: {
    ...mapGetters('seasonesModule', ['seasones'])
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
      this.$store.dispatch('seasonesModule/updateSeasones')
    }
  },
  watch: {
    '$route' (to, from) {
      // this.slug = to.params.slug
      this.loadSeasones()
      // console.log(this.$route.query.page)
    }
  },
  created () {
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
