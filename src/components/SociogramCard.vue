<template>
  <div class="h-screen">
    <v-network-graph
      :zoom-level="0.5"
      :nodes="props.snodes" 
      :edges="props.sedges" 
      :layouts="layouts"
      :configs="configs"> 
      <template>
      </template>
  </v-network-graph>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive} from "vue"
import * as vNG from "v-network-graph"

import {ForceLayout} from "v-network-graph/lib/force-layout"
import type {ForceNodeDatum,ForceEdgeDatum} from "v-network-graph/lib/force-layout"

const props = defineProps({
  snodes: [],
  sedges: []
})
const NODE_COUNT = 2000

const nodes = reactive({})
const edges = reactive({})

// The fixed position of the node can be specified.
const layouts = ref({
  nodes: {
    node0: {
      x: 0,
      y: 0,
      fixed: true, // Unaffected by force
    },
  },
})

const configs = reactive(
  vNG.defineConfigs({
    view: {
      layoutHandler: new ForceLayout({
        positionFixedByDrag: false,
        positionFixedByClickWithAltKey: true,
        createSimulation: (d3, nodes, edges) => {
          // d3-force parameters
          const forceLink = d3.forceLink<ForceNodeDatum, ForceEdgeDatum>(edges).id(d => d.id)
          return d3
            .forceSimulation(nodes)
            .force("edge", forceLink.distance(80).strength(0.05))
            .force("charge", d3.forceManyBody().strength(-300))
            .alphaMin(0.001)
        },
    node: {
      label: {
        visible: true,
        fontFamily: undefined,
        fontSize: 11,
        lineHeight: 1.1,
        color: "#000000",
        margin: 4,
        direction: "south",
        text: "name"
      }
  },
      }),
    },
    node: {
      normal: {
        color: n =>  n.color,
        radius: n => (n.label === "Me" ? 50 : 20)
      },
    },
  })
)

buildNetwork(NODE_COUNT, nodes, edges)

function buildNetwork(count: number, nodes: vNG.Nodes, edges: vNG.Edges) {
  const idNums = [...Array(count)].map((_, i) => i)

  // nodes
  const newNodes = idNums.map(id => [`node${id}`, { id: `node${id}` }])
  Object.assign(nodes, Object.fromEntries(newNodes))

  // edges
  const makeEdgeEntry = (id1: number, id2: number) => {
    return [`edge${id1}-${id2}`, { source: `node${id1}`, target: `node${id2}` }]
  }
  const newEdges = []
  for (let i = 1; i < count; i++) {
    newEdges.push(makeEdgeEntry(Math.floor(i / 4), i))
  }
  Object.assign(edges, Object.fromEntries(newEdges))
}
</script>

<style>
.graph {
  width: 880px;
  height: 600px;
  border: 1px solid #000;
}
</style>
