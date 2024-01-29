<template>
  <q-page class="flex flex-center">
    <h1>Login {{ username}}</h1>

  </q-page>
</template>

<script>
import { useStore } from 'vuex'

export default {
  setup() {
    const store = useStore()
    const username = computed(() => store.auth.getters.username)

    return {
      username
    }
  }
}
</script>
