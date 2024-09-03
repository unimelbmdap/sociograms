<template>
    <main class="container mx-auto my-8 space-y-8">
      <h1 class="text-4xl">Digital photography: mediation, memory and visual communication</h1>
  
      <section class="h-full">    
        <h2 class="text-2xl">Across the practices, platforms and people</h2>
          <div><SociogramCard 
            :nodes="nodes"
            :edges="edges"
          /></div>
      </section>
    </main>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
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
  </script>
  