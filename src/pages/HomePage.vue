<template>
  <q-page class="flex flex-center">
    <h1>Welcome </h1>

  </q-page>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'IndexPage',
  methods: {
    routeHome: function () {
      this.$store.dispatch('routePage', { pageName: '/', url: '' })
    }
  },
  computed: {
    ...mapGetters('auth', [
      'username',
      'currentToken',
      'devFooter'
    ])
  },
}
</script>
