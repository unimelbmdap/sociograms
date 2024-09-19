import { ref } from "vue";
import { useRoute } from "vue-router";

const nodes = ref();
const quotes = ref();
const edges = ref();
const nodesLoading = ref(false);
const route = useRoute();

function fetchData() {
  fetchNodes();
  fetchEdges();
  fetchQuotes();
}

const fetchNodes = async () => {
  nodesLoading.value = true;
  try {
    const response = await fetch("http://localhost:3001/nodes");
    nodes.value = await response.json();
  } finally {
    nodesLoading.value = false;
  }
};

const fetchQuotes = async () => {
  try {
    const response = await fetch("http://localhost:3001/quotes");
    quotes.value = await response.json();
  } finally {
    console.log("got quotes");
  }
};

const fetchEdges = async () => {
  try {
    const response = await fetch("http://localhost:3001/edges");
    edges.value = await response.json();
  } finally {
    console.log("got edges");
  }
};

export default function useNodes() {
  return {
    nodes,
    edges,
    quotes,
    nodesLoading,
    fetchData
  };
}
