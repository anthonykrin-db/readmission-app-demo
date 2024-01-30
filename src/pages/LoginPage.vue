
<script setup lang="js">
import { useAuthStore } from '../store/authStore'
const authStore = useAuthStore()
console.log("Username: "+authStore.username)
</script>
<template>
  <q-page class="flex flex-center">


    <q-card class="q-pa-md shadow-2 my_card" bordered>
      <q-card-section class="text-center">
        <div class="text-grey-9 text-h5 text-weight-bold">Welcome</div>
        <div v-if="authStore.username === 'Guest'">
          <!-- if true, render a link to login page -->
          <div class="text-grey-8">Sign in below to access your account</div>
        </div>
        <div v-else>
          <!-- if false, render a personalized message -->
          <p>Welcome, {{authStore.username}}</p>
          <div class="text-grey-8">Sign in below to reauthenticate</div>
        </div>

      </q-card-section>
      <q-card-section>
        <q-input dense outlined v-model="username" label="Username"></q-input>
        <q-input dense outlined class="q-mt-md" v-model="password" type="password" label="Password"></q-input>
      </q-card-section>
      <q-card-section>
        <q-btn style="
  border-radius: 8px;" color="dark" rounded size="md" label="Sign in" no-caps class="full-width" ></q-btn>
      </q-card-section>
      <q-card-section class="text-center q-pt-none">
        <div class="text-grey-8">Don't have an account yet?
          <router-link to="/register">Sign up</router-link></div>
      </q-card-section>

    </q-card>
  </q-page>
</template>
