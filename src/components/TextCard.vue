<template>
  <span>
    <div
      class="border border-gray-200 bg-white rounded-md"
      @mouseover="$emit('mouseover')"
      @mouseleave="$emit('mouseleave')"
      @click="$emit('clickit')"
    >
      <div v-if=theirFile><img :src=fullname></div>
      <div class="p-4 border-b border-gray-200 bg-white">{{ showQuote }}</div>
      <div class="p-4">{{ node }}</div>
    </div>
  </span>
</template>

<script setup>
import { computed } from 'vue'
const props = defineProps({
  personID: Number,
  theirQuote: String,
  node: String,
  theirFile: String
})

const fullname = computed(() => { 
  return "/src/assets/" + props.theirFile
})

const showQuote = computed(() => {
  return props.theirQuote.substring(0, 500)
})

defineEmits(['mouseover', 'mouseleave', 'clickit'])
</script>

<style scoped>
span:hover {
  background: green;
}
</style>
