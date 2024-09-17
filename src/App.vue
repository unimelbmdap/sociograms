<template>
  <main class="container mx-auto my-8 space-y-8">
    <h1 class="text-4xl">Digital photography: mediation, memory and visual communication</h1>

    <section class="min-h-96">    
      <h2 class="text-2xl">Across the practices, platforms and people</h2>
        <div><SociogramCard
          :snodes="nodes"
          :sedges="filteredEdges"
        /></div>
    </section>
    <section>
      <h2 class="text-2xl">Individuals' social sharing practices for personal photography</h2>

      <div class="grid grid-cols-6 gap-8">
      <TextCard
        @mouseover="hover = true"
        @mouseleave="hover = false"
        @clickit="hover = true"
        v-for="quote in filteredQuotes"
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
import { onMounted, computed } from 'vue'
import TextCard from '@/components/TextCard.vue'
import SociogramCard from '@/components/SociogramCard.vue'
import chooseNodes from '@/composables/chooseNodes'

const { nodes,
        filteredNodes, 
        filteredEdges,
        filteredQuotes,
        nodesLoading, 
        fetchData} = chooseNodes()

onMounted(() => {
  fetchData()
})

</script>
