<template>
  <div id="app">
    <main-layout>
      <router-view/>
    </main-layout>
  </div>
</template>

<script>
import MainLayout from '@/layouts/MainLayout.vue';

export default {
  name: 'App',
  components: {
    MainLayout
  }
}
</script>

<style>
</style>
