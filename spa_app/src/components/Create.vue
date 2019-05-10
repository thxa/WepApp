<template>
  <div class="">
    <div class="">
      <div class="is-size">Season</div>
        Name <input class="input" type="text" v-model="season.name">
        <!-- Category
        <div  class="select is-fullwidth">
          <select class="select" v-model="season.category">
            <option></option>
          </select>
        </div> -->
    Number of episodes
     <input class="input" type="number" v-model="season.number_of_episodes">
        photo url <input class="input" type="url" v-model="season.photo_url">
      <button class="button" v-on:click="createSeason()">send</button>
      <!-- is-loading -->
    </div>
    <hr>
    <div class="">
    <div class="">
      <div class="is-size">episode</div>
        Name <input class="input" type="text" v-model="episode.name">
        </div>
     photo url <input class="input" type="url" v-model="episode.photo_url">
     Video url <input class="input" type="url" v-model="episode.url">
     season
     <div class="select is-rounded">
     <select v-model="episode.season">
       <option
       v-for="season in seasones"
       v-bind:key="season.id">{{season.slug}}</option>
     </select>
   </div>
      <button class="button" v-on:click="createEpisode()">send</button>
      <!-- is-loading -->
    </div>
  </div>
</template>

<script>
import api from '@/api/index.js'
export default {
  name: 'Create',
  data () {
    return {
      season: {
        'name': '',
        'photo_url': '',
        'number_of_episodes': 1
        // 'category': []
        // 'episodes': [
        //   // {
        //   //   'name': '',
        //   //   'photo_url': '',
        //   //   'url': '',
        //   //   'season': 'slug'
        //   // }
        // ]
      },
      episode: {
        'name': '',
        'photo_url': '',
        'url': '',
        'season': ''
      },
      slug: '',
      seasones: []
    }
  },
  methods: {
    createSeason () {
      api.postSeason(this.season)
        .then(data => {
          console.log(data)
        })
        .catch(error => {
          console.log(error)
        })
    },
    createEpisode () {
      api.postVideo(this.episode)
        .then(data => {
          console.log(data)
        })
        .catch(error => {
          console.log(error)
        })
    },
    getSeasonSlug () {
      api.getSeasones()
        .then(data => {
          console.log(data)
          this.seasones = data
        })
    }
  },
  // watch: {
  //   '$route' (to, from) {
  //     // this.slug = to.params.slug
  //     this.createSeason()
  //     // console.log(this.$route.query.page)
  //   }
  // }
  created () {
    this.getSeasonSlug()
  }
}
</script>

<style>
</style>
