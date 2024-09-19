<template>
  <section>
    <h2 class="text-2xl">
      Individuals' social sharing practices for personal photography
    </h2>
    <div>
      This view thinks it showing quotes for node
      {{ $route.params.selectedNode }}
    </div>

    <div v-if="filteredQuotes" class="grid grid-cols-6 gap-8">
      <TextCard
        v-for="quote in filteredQuotes"
        :key="quote.id"
        :personID="quote.PersonID"
        :theirQuote="quote.Quote"
        :node="quote.Node"
        :theirFile="quote.File"
      />
    </div>
    <div v-else>
      <p>
        No quotes to show here, please click on another node from the graph
        above
      </p>
    </div>
  </section>
</template>

<script setup lang="ts">
import { computed } from "vue";
import TextCard from "@/components/TextCard.vue";
import { useRoute } from "vue-router";
import useNodes from "@/composables/useNodes";

const route = useRoute();

console.log("********");
// console.log('filter by '+route.params.selectedNode)

const { quotes} = useNodes();

  let filteredQuotes = quotes;
/*
const filteredQuotes = computed(() =>
  quotes.value.filter((q) => q.Node === route.params.selectedNode)
)
 
  const filteredQuotes = computed(() => {
  if (!route.params.selectedNode) {
    return []; // Return an empty array if selectedNode is not defined
  }
  return quotes.filter((q) => q.Node === route.params.selectedNode);
});
 */

</script>
