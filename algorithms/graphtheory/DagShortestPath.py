'''
This Algo finds the shortest path for a DAG
Time complexity : O(V+E)
'''
from collections import defaultdict
from TopologicalSortAdjacencyList import TopologicalSortAdjacencyList
from TopologicalSortAdjacencyList import Graph as TpGraph


class Graph(object):
    def __init__(self):
        self.adjacencyList = defaultdict(list)
        self.tpgraph = TpGraph()
        #self.adjacencyListWithoutWeight = defaultdict(list)

    def addEdge(self, u, v, w):
        self.adjacencyList[u].append((v, w))
        self.tpgraph.addEdge(u, v)

    def getGraphWithoutWeight(self):
        return self.tpgraph

    def getNeighbours(self, u):
        return self.adjacencyList[u]

    def getLength(self):
        return len(self.adjacencyList.keys())


class DagShortestPath(object):
    def __init__(self, g):
        self.graph = g
        self.length = g.getLength()

    def ssps(self, start_node):
        topo = TopologicalSortAdjacencyList(self.graph.getGraphWithoutWeight())
        topoSortArray = topo.topSort()

        dist = [None] * (self.length)
        dist[start_node] = 0

        # relaxin phase

        counter = 0
        while counter < self.length:
            node = topoSortArray[counter]
            edges = self.graph.getNeighbours(node)
            if len(edges) != 0:
                for to_node, weight in edges:
                    newDist = dist[node] + weight
                    if dist[to_node] == None:
                        dist[to_node] = newDist
                    else:
                        dist[to_node] = min(
                            dist[to_node], newDist)
            counter += 1
        return dist


def main():
    g = Graph()
    g.addEdge(0, 1, 3)
    g.addEdge(0, 2, 6)
    g.addEdge(1, 2, 4)
    g.addEdge(1, 3, 4)
    g.addEdge(1, 4, 11)
    g.addEdge(2, 3, 5)
    g.addEdge(2, 6, 11)
    g.addEdge(3, 4, -4)
    g.addEdge(3, 5, 5)
    g.addEdge(3, 6, 2)
    g.addEdge(4, 4, 0)
    g.addEdge(5, 5, 0)
    g.addEdge(6, 6, 0)

    dagssps = DagShortestPath(g)
    dist = dagssps.ssps(0)

    print(dist)


if __name__ == "__main__":
    main()
