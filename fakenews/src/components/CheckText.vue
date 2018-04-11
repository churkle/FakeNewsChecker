<template>
  <div class="checktext">
    <h1>{{ msg }}</h1>
    <v-container fluid>
      <v-layout row>
        <v-flex xs2>
        </v-flex>
        <v-flex xs6>
          <v-text-field
              name="articleTextField"
              label="Paste article here"
              id="articleTextField"
              v-model="article"
              multi-line
          ></v-text-field>
        </v-flex>
        <v-btn v-on:click="getResult()" normal>Go!</v-btn>
        <div class="text-xs-center">
          <v-btn v-on:click="changeMode()" normal>Check URL</v-btn>
        </div>
      </v-layout>
      <p>{{ result }}</p>
    </v-container>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CheckText',
  data () {
    return {
      msg: 'Fake News Checker',
      article: '',
      result: ''
    }
  },
  methods: {
    getResult () {
      this.result = 'Checking... please wait'
      axios.post('http://34.229.13.101:5000/checktext', {
        text: this.article
      })
        .then((data) => {
          this.result = `Article is: ${data.data['message'][0]}`
        })
    },
    changeMode () {
      this.$router.push('/')
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
