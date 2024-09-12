<template>
  <main class="container mx-auto my-8 space-y-8">
    <h1 class="text-4xl">Digital photography: mediation, memory and visual communication</h1>

    <section class="min-h-96">    
      <h2 class="text-2xl">Across the practices, platforms and people</h2>
        <div><SociogramCard 
          :snodes="nodes"
          :sedges="edges"
          :selectedNodes="filteredNodes"
          @selectInstaNode="console.log('filter to instagram node')"
        /></div>
        <div v-if="filteredNodes">{{filteredNodes}}</div>
    </section>
    <section>
      <h2 class="text-2xl">Individuals' social sharing practices for personal photography</h2>

      <div class="grid grid-cols-6 gap-8">
      <TextCard
        @mouseover="hover = true"
        @mouseleave="hover = false"
        @clickit="hover = true"
        v-for="quote in quotes"
          :key="quote.id"
          :personID="quote.PersonID"
          :theirQuote="quote.Quote"
          :node="quote.Node"
          :theirFile="quote.File"
      /></div>
    </section>
  </main>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import TextCard from '@/components/TextCard.vue'
import SociogramCard from '@/components/SociogramCard.vue'

const quotes = ref()
const nodes = ref()
const edges = ref()

const fetchNodes = async () => {
  const response = await fetch('http://localhost:3001/nodes')
  nodes.value = await response.json()
}
const fetchQuotes = async () => {
  const response = await fetch('http://localhost:3001/quotes')
  quotes.value = await response.json()
}
const fetchEdges = async () => {
  const response = await fetch('http://localhost:3001/edges')
  edges.value = await response.json()
}

onMounted(() => {
  fetchQuotes()
  fetchNodes()
  fetchEdges()
})

const hover = ref(false)
const filteredNodes = ref([])

/*
const filteredQuotes = computed(
  ()=> {
    quotes.value.filter(
      quote => quote.Node === 'Instagram'
    )
  }
)
*/
</script>
