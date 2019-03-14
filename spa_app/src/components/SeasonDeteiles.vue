<template>
  <div class="container main section">
    <div class="title is-centerd">
      name: {{season.name}}
    </div>
    <div class="">
      <img :src="season.photo_url">
    </div>
    <div class="footer">
            slug: {{season.slug}}
      <div class="columns">
        <div class="column" v-for="episod in episodes"
        v-bind:key="episod.id">
        {{episod.id}}
        </div>
      </div>

    </div>
  </div>
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
      season: {}
    }
  },
  methods: {
    loadSeason () {
      // if (this.slug === 'movie') {
      //   this.seasones = this.movie
      // } else {
      //   this.seasones = this.anime
      // }

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
      this.loadSeason(this.slug)
      console.log(this.$route.query.page)
    }
  },
  created () {
    this.loadSeason(this.slug)
  }
}
</script>
<style>
</style>
