<template>
  <div class="demo-control-panel">
    <label>Selected:</label>
    <el-select
      v-model="selectedNodes"
      placeholder="Select"
    >
      <el-option
        v-for="(node, key) in props.snodes"
        :key="key"
        :label="node.name"
        :value="key"
      />
    </el-select></div>
  <div class="h-full">
    <v-network-graph
      :zoom-level="0.5"
      :nodes="props.snodes" 
      :edges="props.sedges" 
      :layouts="layouts"
      :configs="configs"
      :selected-nodes="selectedNodes"> 
  </v-network-graph>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, watch} from "vue"
import * as vNG from "v-network-graph"

import {ForceLayout} from "v-network-graph/lib/force-layout"
import type {ForceNodeDatum,ForceEdgeDatum} from "v-network-graph/lib/force-layout"

const props = defineProps({
  snodes: [],
  sedges: []
})

defineEmits(['selectedNodes'])

const nodes = reactive({})
const edges = reactive({})
const selectedNodes = ref<string[]>([])

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
        color: n =>  n.color,
        radius: n => (n.label === "Me" ? 50 : 20)
      },
    },
  })
)
configs.node.selectable=true


</script>

<style>
.graph {
  width: 880px;
  height: 600px;
  border: 1px solid #000;
}
</style>
