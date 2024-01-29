<template><q-item
    clickable
    @click="routeClick(link)"><q-item-section
      v-if="icon"
      avatar
    ><q-icon :name="icon" /></q-item-section><q-item-section><q-item-label>{{ title }}</q-item-label><q-item-label caption>{{ caption }}</q-item-label></q-item-section></q-item>
</template>

<script>
export default {
  name: 'AdminNav',
  props: {
    title: {
      type: String,
      required: true
    },

    caption: {
      type: String,
      default: ''
    },

    link: {
      type: String,
      default: '#'
    },

    icon: {
      type: String,
      default: ''
    }
  },
  methods: {
    routeClick: function (page) {
      this.$router.push(page).catch(err => {
        // Ignore the vuex err regarding  navigating to the page they are already on.
        if (
          err.name !== 'NavigationDuplicated' &&
          !err.message.includes('Avoided redundant navigation to current location')
        ) {
          // But print any other errors to the console
          console.log('Routing error: ' + err)
        }
      })
    }
  }
}
</script>
