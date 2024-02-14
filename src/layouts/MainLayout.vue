
<script>
import { ref } from 'vue'
import AdminNav from "components/AdminNav.vue";
import { useAuthStore } from '../store/authStore'

export default {

  name: 'MainLayout',
  setup() {
    const authStore = useAuthStore()
    const rightDrawerOpen = ref(false)

    return {
      authStore,
      rightDrawerOpen,
      toggleRightDrawer() {
        rightDrawerOpen.value = !rightDrawerOpen.value
      }
    }
  },
  methods: {
    routeHome: function () {
      this.$router.push("/")
    }
  },
  components: {
    AdminNav
  }
}
</script>


<template>
  <q-layout view="hHr lpR fFr">
    <q-header class="bg-primary text-white" height-hint="98">
      <q-toolbar>
        <q-toolbar-title>
          <img src="/logo-readmissions.png" height="20" alt="Readmissions Application"> Readmissions Application
        </q-toolbar-title>
        <q-btn dense flat round align="right" icon="menu" @click="toggleRightDrawer"/>
      </q-toolbar>
    </q-header>

    <q-drawer show-if-above v-model="rightDrawerOpen" side="right" bordered>
      <admin-nav icon="home" link="home" title="Home" />
      <admin-nav icon="person" link="profile" title="My Profile"/>
      <admin-nav icon="settings" link="settings" title="Settings"/>
      <admin-nav icon="tasks" link="tasks" title="Tasks"/>
      <admin-nav icon="warning" link="alerts" title="Alerts"/>
      <admin-nav icon="resources" link="resources" title="Saved Resources"/>
      <admin-nav icon="calendar_month" link="timeline" title="Timeline"/>
      <admin-nav icon="medications" link="medications" title="My Medications"/>
      <admin-nav icon="contacts" link="contacts" title="My Contacts"/>
    </q-drawer>

    <q-page-container>
      <router-view/>
    </q-page-container>

    <q-footer elevated>
      <q-toolbar>
        <admin-nav icon="tasks" link="tasks" title=""/>
        <admin-nav icon="warning" link="alerts" title=""/>
        <admin-nav icon="home" link="home" title="" />
        <admin-nav icon="resources" link="resources" title=""/>
        <admin-nav icon="calendar_month" link="timeline" title=""/>
      </q-toolbar>
      <q-input v-model="authStore.debugFooter" />
    </q-footer>
  </q-layout>
</template>
