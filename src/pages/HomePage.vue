
<script setup lang="js">
import { useAuthStore } from '../store/authStore'
const authStore = useAuthStore()
console.log("Username: "+authStore.username)
</script>
<template>
  <q-page class="flex flex-center">

    <div v-if="authStore.username === 'Guest' || authStore.username === ''">
      <!-- if true, render a link to login page -->
      <p>Welcome, {{authStore.username}}</p>
      Please <router-link to="/login">Login</router-link>
    </div>
    <div v-else>
      <!-- if false, render a personalized message -->
      <p>Welcome, {{authStore.username}}</p>
      You have been authenticated
    </div>

  </q-page>
</template>
