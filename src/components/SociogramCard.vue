<template>

  <div class="h-96">
    <v-network-graph
      :zoom-level="0.5"
      :nodes="nodes" 
      :edges="filteredEdges" 
      :layouts="layouts"
      :configs="configs"
      :event-handlers="eventHandlers"> 
  </v-network-graph>
  </div>

</template>

<script setup lang="ts">
import { ref, reactive} from "vue"
import * as vNG from "v-network-graph"

import {ForceLayout} from "v-network-graph/lib/force-layout"
import type {ForceNodeDatum,ForceEdgeDatum} from "v-network-graph/lib/force-layout"
import chooseNodes from '@/composables/chooseNodes'

const {nodes, filteredNodes, filteredEdges, filterByNode, selectNode} = chooseNodes()

const eventHandlers: vNG.EventHandlers = {
  "node:click": ({ node }) => {
    console.log('clicked a node ')
    filterByNode(node)
  },
}

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
            .force("charge", d3.forceManyBody().strength(-500))
            .force("center", d3.forceCenter().strength(0.05))
            .alphaMin(0.001)
        }
      }),
    },
    node: {
      normal: {
        type: n => n.label === "Me" ? 'circle' : 'rect',
        color: n =>  n.color,
        radius: n => (n.label === "Me" ? 50 : 20)
      },
      selectable: 1,
      label: {
        fontSize: n => n.label === "Me" ? 20 : 11,
        direction: n => n.label === "Me" ? 'center' : 'south'
      }
    },
  })
)

</script>

<style>
.graph {
  width: 880px;
  height: 600px;
  border: 1px solid #000;
}
</style>
