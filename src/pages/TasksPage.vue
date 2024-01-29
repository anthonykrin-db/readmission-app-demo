<template>
  <q-page class="flex flex-center">
    <h1>Profiles {{ $store.getters.username}}</h1>

  </q-page>
</template>

<script>
import { defineComponent } from 'vue'
import {username} from "src/store-vuex/auth/getters";

export default defineComponent({
  name: 'TasksPage',
  methods: {username}
})
</script>
