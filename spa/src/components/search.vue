<template>
  <div class="navbar-item field has-addons">
    <div class="control">
      <div class="dropdown is-active">
        <div class="dropdown-trigger">
          <input class="input is-rounded" v-model="seasonName" v-on:keyup="getResult()" type="text"  placeholder="Find a Season">
        </div>
        <div class="dropdown-menu" id="dropdown-menu" v-if="seasonesResult.length" role="menu">
          <div class="dropdown-content">
            <router-link class="dropdown-item"
            v-for="season in seasonesResult"
            :key="season.name"
            :to="{ name: 'Season', params: { slug: season.slug} }">
               <span>
                 <!-- <i class="fas fa-movie" aria-hidden="true"></i> -->
               </span>
               {{season.name}}
            </router-link>
          </div>
        </div>
      </div>
    </div>
    <div class="control">
      <a class="button is-info">
        <i class="fas fa-search"></i>
      </a>
    </div>
    <!-- <ul v-for="season in seasones" v-bind:key="season.name" >
      <router-link :to="{ name: 'season', params: { slug: season.slug } }">{{ season.name }}</router-link>
    </ul> -->
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import api from '@/api/index.js'
export default {
  name: 'search',
  data () {
    return {
      seasonName: '',
      seasonesResult: []
    }
  },
  // ...mapGetters('searchModule', ['seasonName', 'seasonesResult']),
  methods: {
    getResult (context) {
      if (this.seasonName.length) {
        api.searchSeason(this.seasonName)
          .then(data => {
            this.seasonesResult = data
          })
        // this.$store.dispatch('searchModule/searchSeason', this.seasonName)
      }
        this.seasonesResult = []
    }
  }
}
</script>

<style lang="sass">

  // color
  $white: hsl(0, 0%, 100%)
  $radius: 4px

  $dropdown-menu-min-width: 12rem
  $dropdown-content-background-color: $white
  $dropdown-content-radius: $radius
  $dropdown-content-offset: 10px
  // input[type=text] {
  //   width: 130px;
  //   -webkit-transition: width 0.4s ease-in-out;
  //   transition: width 0.4s ease-in-out;
  // }
  //
  // /* When the input field gets focus, change its width to 100% */
  // input[type=text]:focus {
  //   width: 100%;
  // }
</style>
