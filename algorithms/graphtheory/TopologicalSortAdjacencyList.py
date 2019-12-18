'''
This topological sort implementation takes an adjacency list of an acyclic graph and returns an
array with the indexes of the nodes in a (non unique) topological order which tells you how to
process the nodes in the graph. More precisely from wiki: A topological ordering is a linear
ordering of its vertices such that for every directed edge uv from vertex u to vertex v, u comes
before v in the ordering.

Time Complexity : O(V+E)
'''

from collections import defaultdict


class Graph:
    def __init__(self):
        self.adjacencyList = defaultdict(list)

    def addEdge(self, u, v):
        self.adjacencyList[u].append(v)

    def getLength(self):
        return len(self.adjacencyList.keys())

    def getNeighbours(self, u):
        return self.adjacencyList[u]


class TopologicalSortAdjacencyList:
    def __init__(self, g):
        self.graph = g
        self.n = g.getLength()
        self.visited = [False] * (self.graph.getLength())
        self.ordering = [None] * (self.graph.getLength())
        self.i = self.graph.getLength() - 1

    def topSort(self):
        at = 0
        while at < self.n:
            if self.visited[at] == False:
                visitedNodes = []
                self.dfs(at, visitedNodes)
                for nodeID in visitedNodes:
                    self.ordering[self.i] = nodeID
                    self.i -= 1
            at += 1
        return self.ordering

    def dfs(self, at, visitedNodes):
        self.visited[at] = True
        edges = self.graph.getNeighbours(at)
        for edge in edges:
            if self.visited[edge] == False:
                self.dfs(edge, visitedNodes)
        visitedNodes.append(at)


def main():
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    topo = TopologicalSortAdjacencyList(g)
    print(topo.topSort())


if __name__ == "__main__":
    main()
