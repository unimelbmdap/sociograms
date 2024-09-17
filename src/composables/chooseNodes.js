import {ref} from 'vue'

const nodes = ref()
const quotes = ref()
const edges = ref()
let filteredNodes=ref()
let filteredQuotes=ref()
let filteredEdges=ref()
const nodesLoading = ref(false)
const edgesLoading = ref(false)
const quotesLoading = ref(false)
const selectNode=ref()

function fetchData() {
    fetchNodes()
    fetchEdges()
    fetchQuotes()
}

const fetchNodes = async () => {
    nodesLoading.value=true
    try {
        const response = await fetch('http://localhost:3001/nodes')
        nodes.value = await response.json()
    } finally {
        nodesLoading.value=false
        filteredNodes.value = nodes.value
        /*
        filteredNodes =nodes.filter((item) =>
            item.label === "Instagram"
        */
        console.log('filter da nodes')
        console.log(filteredNodes.value)
    }
  }

const fetchQuotes = async () => {
    quotesLoading.value=true
    try{
        const response = await fetch('http://localhost:3001/quotes')
        quotes.value = await response.json()
    } finally {
        quotesLoading.value=false
        filteredQuotes.value = quotes.value
    }
  }

  const fetchEdges = async () => {
    edgesLoading.value=true
    try{
        const response = await fetch('http://localhost:3001/edges')
        edges.value = await response.json()
    } finally {
        edgesLoading.value=false
        filteredEdges.value = edges.value
    }
  }

  function filterByNode(selectNode) {
    console.log('filter by ')
    console.log(selectNode)
  }

export default function chooseNodes()
{
    return {
        nodes,
        selectNode,
        filteredNodes,
        filteredEdges,
        filteredQuotes,
        nodesLoading,
        fetchData,
        filterByNode
    }
}