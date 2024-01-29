<template>
  <q-page class="flex flex-center">
    <h1>My Contacts {{ $store.getters.username}}</h1>

  </q-page>
</template>

<script>
import { defineComponent } from 'vue'
import {username} from "src/store/auth/getters";

export default defineComponent({
  name: 'MyContactsPage',
  methods: {username}
})
</script>
