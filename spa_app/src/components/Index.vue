<template>
  <main class="main">
    <div class="container">
      <div class="columns is-desktop is-mobile">
        <router-link
        :to="{ name: 'Season', params: { slug: season.slug} }" class="column  is-one-quarters" v-for="season in seasones"
        v-bind:key="season.id">
          <season :link="season.link">
            <h3 slot="name">{{season.name}}</h3>
            <img slot="photo_url" :src="season.photo_url">
          </season>
          </router-link>
        </div>
      </div>
  </main>
</template>

<script>
import Season from '@/components/Season.vue'
import api from '@/api/index.js'
export default {
  name: 'Index',
  components: {
    'season': Season
  },
  data () {
    return {
      slug: this.$route.params.slug,
      seasones: []
    }
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
      api.getSeasones()
        .then(data => {
          console.log(data)
          this.seasones = data
        })
    }
  },
  watch: {
    '$route' (to, from) {
      this.slug = to.params.slug
      this.loadSeasones()
      console.log(this.$route.query.page)
    }
  },
  created () {
    this.loadSeasones()
  }
}
</script>

<style>
.main {
  margin: 5%;
  /* background-color: black; */
}
.columns {
  flex-wrap: wrap;
}
.column {
  /* margin: 1%; */
  /* background-color: blue; */
  /* border: solid 1px black; */

}
</style>
