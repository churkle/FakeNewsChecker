<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <v-container fluid>
      <v-layout row>
        <v-flex xs3>
        </v-flex>
        <v-flex xs6>
          <v-text-field
              name="urlTextField"
              label="URL"
              id="urlTextField"
              v-model="url"
          ></v-text-field>
        </v-flex>
        <v-btn normal>Go!</v-btn>
      </v-layout>
      <p>URL is: {{ url }}</p>
    </v-container>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Fake News Checker',
      url: ''
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
