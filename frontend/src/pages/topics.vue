<template>
  <div class="topics">
    <ul>
      <li v-for="(topic, index) in topics" :key="index" style="display:block">
        {{index}}-{{topic}}
      </li>
    </ul>
  </div>
</template>

<script>
import { getTopics } from '../api/api'
export default {
  name: 'Topics',
  data () {
    return {
      topics: []
    }
  },
  methods: {
    loadBooks () {
      getTopics().then(res => {
        console.log(res.data)
        this.topics = res.data
      })
    }
  },
  created: function () {
    this.loadBooks()
  }
}
</script>