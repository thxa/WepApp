<template>
  <div class="card">
    <slot name="name"></slot>
    <slot name="photo_url"></slot>
  </div>
</template>

<script>
export default {
  props: ['link']
}
</script>

<style>
.card: {
  /* padding-bottom: 40px; */
  height: 100%;
}
</style>
