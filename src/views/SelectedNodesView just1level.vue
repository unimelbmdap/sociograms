<template>

    <h2 class="text-2xl">
      Individuals' social sharing practices through
      {{ $route.params.selectedNode }}
    </h2>

  <section>
    <div>{{adjacencyList}}</div>
    <div><SociogramCard :snodes="filteredNodes" :sedges="edges" /></div>
  </section>
  <section>
    <div v-if="filteredQuotes" class="grid grid-cols-2 gap-8">
      <TextCard
        v-for="(quote, index) in filteredQuotes"
        :key="index"
        :personID="quote.PersonID"
        :theirQuote="quote.Quote"
        :node="quote.Node"
        :theirFile="quote.File"
      />
    </div>
    <div v-else>
      <p>
        No quotes to show yet, please click on a node from the graph
        above
      </p>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref,computed , onMounted, watch} from "vue";
import TextCard from "@/components/TextCard.vue";
import { useRoute } from "vue-router";
import useNodes from "@/composables/useNodes";
import SociogramCard from "@/components/SociogramCard.vue";

const route = useRoute();
const { nodes, quotes, edges, nodesLoading } = useNodes();

const filteredQuotes = computed(() => {
  if (!route.params.selectedNode) {
    return []; // Return an empty array if selectedNode is not defined
  }
  return quotes.value
    .filter((q) => q.Node === route.params.selectedNode)
    .sort((a, b) => a.Quote.length - b.Quote.length);
});


const filteredEdges = computed(() => {
  console.log("filtering the nodes");
  if (nodesLoading.value || !edges.value) {
    return []; // Return an empty array if loading or not an array
  }
  // Convert the object into an array and filter
  return Object.values(edges.value).filter((edges) => {
    return edges.source === route.params.selectedNode; // select edges connected from the selected node
  });
});


// its Friday arvo so this is good for now
const connectedNodes = computed(() => {
  // Check if edges is an object
  if (!filteredEdges.value || typeof filteredEdges.value !== "object") {
    console.warn("edges.value is not an object:", filteredEdges.value);
    return []; // Return an empty array if not valid
  }
  // Transform the edges object to an array and extract target values
  const targets = Object.values(filteredEdges.value).map((edge) => edge.target);
  // Ensure the result is an array
  return Array.isArray(targets) ? targets : [];
});


const filteredNodes = computed(() => {
  console.log("filtering the nodes");
  //connectedNodes.value.push("Me")
  connectedNodes.value.push(route.params.selectedNode);

  // Ensure nodes are loaded and valid
  if (nodesLoading.value || !nodes.value) {
    return {}; // Return an empty object if loading or not valid
  }

  // Initialize an empty object to hold the filtered results
  const result = {};

  // Use Object.entries to iterate through key-value pairs
  Object.entries(nodes.value).forEach(([key, node]) => {
    if (connectedNodes.value.includes(node.name)) {
      // Add each matching node to the result object
      result[key] = { ...node }; // Spread to ensure a new object is created
    }
  });

  return result; // Return the result object containing filtered nodes
});

</script>
