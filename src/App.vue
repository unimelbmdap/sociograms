<template>
  <main class="container mx-auto my-8 space-y-8">
    <h1 class="text-4xl">
      Digital photography: mediation, memory and visual communication
    </h1>

    <section class="min-h-96">
      <h2 class="text-2xl">Across the practices, platforms and people</h2>
      <div><SociogramCard :snodes="nodes" :sedges="edges" /></div>
    </section>
    <RouterView />
  </main>
</template>

<script setup>
import { onMounted, computed } from "vue";
import SociogramCard from "@/components/SociogramCard.vue";
import useNodes from "@/composables/useNodes";

const { nodes, edges, quotes, nodesLoading, fetchData } = useNodes();

onMounted(() => {
  fetchData();
});

</script>
