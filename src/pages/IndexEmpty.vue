<template>
  <div>
    <h1>Hello {{ message }}</h1>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: "Welcome to the new Vue.js Page!"
    };
  }
};
</script>

<style scoped>
h1 {
  color: blue;
}
</style>
