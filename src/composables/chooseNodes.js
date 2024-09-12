import {ref} from 'vue'

const filteredNodes=ref([])
const nodesLoading = ref(false)

const fetchNodes = async () => {
    loading.value=true
    try {
        const response = await fetch('http://localhost:3001/nodes')
        nodes.value = await response.json()
    } finally {
        loading.value=false
    }
  }

export default function chooseNodes()
{
    return {
        filteredNodes,
        loading,
        fetchNodes
    }
}