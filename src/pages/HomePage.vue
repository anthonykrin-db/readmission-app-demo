
<script setup lang="js">
import { useAuthStore } from '../store/authStore'
const authStore = useAuthStore()
console.log("Username: "+authStore.username)
</script>
<template>
  <q-page class="flex flex-center">
    <h1>Welcome {{authStore.username}}!</h1>
  </q-page>
</template>
