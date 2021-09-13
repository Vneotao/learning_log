<template>
  <div class="index">
    <img src="../assets/logo.png">
    <h1>{{ msg }}</h1>
    <h2>{{ msg1 }}</h2>
  </div>
</template>

<script>
export default {
  name: 'index',
  data () {
    return {
      msg: 'Welcome to Learning Logs',
      msg1: "Learning Log helps you keep track of your learning, for any topic you're learning about."
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
