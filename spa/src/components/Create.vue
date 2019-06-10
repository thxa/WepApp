<template>
  <div class="">
    <div class="">
      <div class="is-size">Season</div>
        Name <input class="input" type="text" v-model="newSeason.name">
        <!-- Category
        <div  class="select is-fullwidth">
          <select class="select" v-model="season.category">
            <option></option>
          </select>
        </div> -->
    Number of episodes
     <input class="input" type="number" v-model="newSeason.number_of_episodes">
        photo url <input class="input input-url" type="url" v-model="newSeason.photo_url">
      <button class="button" v-on:click="createSeason()">send</button>
      <!-- is-loading -->
    </div>
    <!-- <hr>
    <div>
      <div>episode</div>
       Name <input class="input" type="text" v-model="episode.name">
       photo url <input class="input" type="url" v-model="episode.photo_url">
       Video url <input class="input" type="url" v-model="episode.url">
        <button class="button" v-on:click="createEpisode()">send</button>
        is-loading

      </div> -->
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'Create',
  computed: {
    ...mapGetters('seasonModule', ['newSeason'])
  },
  methods: {
    createSeason () {
      this.$store.dispatch('seasonModule/createSeason', this.newSeason)
    }
  }
  // watch: {
  //   '$route' (to, from) {
  //     // this.slug = to.params.slug
  //     this.createSeason()
  //     // console.log(this.$route.query.page)
  //   }
  // }
  // created () {
  // }
}
</script>

<style>
</style>
