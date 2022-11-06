class GraphNode {
  val = 0
  neighbors = []
  constructor(val = 0, neighbors = []) {
    this.val = val
    this.neighbors = neighbors
  }
}

function cloneGraph(node) {
  if(node == undefined || node == null) {
    return null
  }
  let stack = [node]
  let edgeMap = {}
  let edgeArray = []
  let visited = {}
  while(stack.length > 0) {
    let graphPoint = stack.pop()
    if(visited[graphPoint.val]) {
      continue
    }
    visited[graphPoint.val] = true
    if(edgeMap[graphPoint.val] == undefined) {
      edgeMap[graphPoint.val] = []
    }
    for(let neighbor of graphPoint.neighbors) {
      stack.push(neighbor)
      edgeMap[graphPoint.val].push(neighbor.val)
    }
  }
  for(let i = 1; i <= Object.keys(edgeMap).length; i++) {
    edgeArray.push(edgeMap[i])
  }
  return edgesToGraph(edgeArray)
}

function edgesToGraph(edges) {
  if(edges.length == 0) {
    return null
  }
  let graphMap = {}
  for(let i = 0; i < edges.length; i++) {
    let neighbors = edges[i]
    if(graphMap[i+1] == undefined) {
      graphMap[i+1] = new GraphNode(i+1)
    }
    for(let neighbor of neighbors) {
      if(graphMap[neighbor] == undefined) {
        graphMap[neighbor] = new GraphNode(neighbor)
      }
    }
    for(let node of neighbors) {
      graphMap[i+1].neighbors.push(graphMap[node])
    }
  }
  return graphMap[1]
}

let edgeArray = [[2,3,4],[1,3,4],[1,2,4],[1,2,3]]

let graph = edgesToGraph(edgeArray)
let cloned = cloneGraph(graph)

console.log(graph, cloned)
