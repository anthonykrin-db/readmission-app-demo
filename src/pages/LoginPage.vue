<script setup lang="js">
import {useAuthStore} from '../store/authStore'
import {reactive, ref} from 'vue';

const authStore = useAuthStore();
const userCredentials = reactive({username: authStore.username, password: ''});
const loginError = ref(false);
const loginSuccess = ref(false);
const loginErrorMessage = ref('');
const resetLoginStatus = () => {
  loginError.value = false;
  loginSuccess.value = false;
  loginErrorMessage.value = '';
  authStore.username = '';
  userCredentials.username = '';
  userCredentials.password = '';
};

const login = async () => {
  //console.log("Username: "+userCredentials.username+", password: "+userCredentials.password)
  authStore.login(userCredentials).then((result) => {
    if (result) {
      console.log('Login was successful');
      loginSuccess.value = true;
      // handle login success
      loginErrorMessage.value = '';
    } else {
      console.log('Login unsuccessful');
      // handle login failure
      loginError.value = true;
      loginErrorMessage.value = 'Login failed. Please check your credentials.';
    }
  })
    .catch((error) => {
      console.log('Authentication handing error occurred:', error);
      // handle error
      loginError.value = true;
      loginErrorMessage.value = 'Login error: '+error.message;
    });
};
const logout = async () => {
  resetLoginStatus();
  const success = await authStore.logout();
  if (success) {
    loginSuccess.value = false;
  } else {
    loginError.value = true;
    loginErrorMessage.value = 'Logout failed.';
  }
};

</script>
<template>
  <q-page class="flex flex-center">

    <q-card class="q-pa-md shadow-2 my_card" bordered>
      <q-card-section class="text-center">
        <div v-if="userCredentials.username === 'Guest' || userCredentials.username === ''">
          <!-- if true, render a link to login page -->
          <div class="text-grey-8">Sign in below to access your account</div>
        </div>
        <div v-else>
          <div v-if="loginSuccess">
            <!-- if false, render a personalized message -->
            <p>Welcome, {{ userCredentials.username }}</p>
          </div>
          <div v-else>
            <div class="text-grey-8">Sign in below to reauthenticate</div>
          </div>
        </div>

      </q-card-section>
      <q-card-section>
        <q-input dense outlined v-model="userCredentials.username" label="Username"></q-input>
        <q-input dense outlined class="q-mt-md" v-model="userCredentials.password" type="password"
                 label="Password"></q-input>
      </q-card-section>
      <q-card-section>
        <q-btn style="
  border-radius: 8px;" color="dark" rounded size="md" label="Sign in" no-caps class="full-width" @click="login"></q-btn>
      </q-card-section>
      <q-card-section class="text-center q-pt-none">
        <div v-if="loginError" style="color: red;">{{ loginErrorMessage }}</div>
        <div v-if="loginSuccess" style="color: green;">Login successful!</div>
        <div class="text-grey-8">Don't have an account yet?
          <router-link to="/register">Sign up</router-link>
        </div>
        <div v-if="loginSuccess">
          <q-btn style="
  border-radius: 8px;" color="dark" rounded size="md" label="Logout" no-caps class="full-width" @click="logout"></q-btn>
        </div>
      </q-card-section>
    </q-card>

  </q-page>
</template>
