<template>
  <main class="container mx-auto my-8 space-y-8">
    <h1 class="text-4xl">Digital photography: mediation, memory and visual communication</h1>

    <section>    
      <h2 class="text-2xl">Across the practices, platforms and people</h2>
        <div v-if="simple"  class="h-96"><SociogramCard 
          :snodes="nodes"
          :sedges="edges"
        /></div>
    </section>
    <section>
      <h2 class="text-2xl">Individuals' social sharing practices for personal photography</h2>

      <div class="grid grid-cols-6 gap-8" v-if="quotesLoaded">
      <TextCard
        v-for="quote in quotes"
        :key="quote.id"
        :personID="quote.PersonID"
        :theirQuote="quote.Quote"
        :node="quote.Node"
        :theirFile="quote.File"
      /></div>
      <div v-else>
        <p>No quotes to show</p>
      </div>
    </section>
  </main>
</template>

<script setup>
import { ref, onMounted, computed} from 'vue'
import TextCard from '@/components/TextCard.vue'
import SociogramCard from '@/components/SociogramCard.vue'

const quotes = ref()
const nodes = ref()
const edges = ref()

let simple = true
let dataLoaded = ref(false)
let quotesLoaded = ref(false)

const fetchNodes = async () => {
  try {
  const response = await fetch('http://localhost:3001/nodes')
  nodes.value = await response.json()
} finally {
  dataLoaded = true
}
}
const fetchQuotes = async () => {
  try{
  const response = await fetch('http://localhost:3001/quotes')
  quotes.value = await response.json()
  } finally {
    quotesLoaded = true  }
}
const fetchEdges = async () => {
  const response = await fetch('http://localhost:3001/edges')
  edges.value = await response.json()
}

onMounted(() => {
  fetchNodes()
  fetchQuotes()
  fetchEdges()
})

// next add if simple=true then filter
/*
const simpleNodes = computed(
  ()=> 
    nodes.value.filter(
    item => (item.level <3))
) 
*/

const filteredQuotes = computed(
  ()=> quotes.value.filter(
    quote => (quote.Node == "BeReal")
  )
)

const hover = ref(false)
</script>
