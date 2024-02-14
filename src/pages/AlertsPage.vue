<script>
import { defineComponent } from 'vue'
import { useAuthStore } from '../store/authStore'
const authStore = useAuthStore()

export default defineComponent({
  name: 'AlertsPage'
})
</script>

<template>
  <q-page class="flex flex-center">
    <h1>Alerts </h1>


  </q-page>
</template>


