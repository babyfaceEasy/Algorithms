'''
This file contains an algorithm to find all connected components of an undirected graph.
If the graph you're dealing is directed have a look at Tarjan's algorithm to find strongly 
connected components.

@author Olakunle Odegbaro, oodegbaro@gmail.com
'''
from collections import defaultdict


class Graph:
    def __init__(self):
        self.adjacencyList = defaultdict(list)

    def addEdge(self, u, v):
        self.adjacencyList[u].append(v)

    def getNode(self, node):
        return self.adjacencyList[node]

    def getGraph(self):
        return self.adjacencyList

    def length(self):
        return len(self.adjacencyList.keys())


class ConnectedComponentsDfsSolverAdjacencyList:
    def __init__(self, g):
        self.graph = g
        self.graphLength = g.length()
        self.visited = [False] * (self.graphLength)
        self.componentCount = 0
        self.component = [-1] * (self.graphLength)

    def dfs(self, node):
        if self.visited[node] == False:
            self.visited[node] = True
            self.component[node] = self.componentCount
            for next_node in self.graph.getNode(node):
                self.dfs(next_node)

    def findComponent(self, node):
        for node in range(self.graphLength):
            if not self.visited[node]:
                self.componentCount += 1
                self.dfs(node)
        return (self.componentCount, self.component)


def main():
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    g.addEdge(4, 4)

    componentsCountObj = ConnectedComponentsDfsSolverAdjacencyList(g)
    (count, components) = componentsCountObj.findComponent(0)

    print(
        f'Total number of connected components {count}, Vetices belongs to components: {components}'
    )


if __name__ == "__main__":
    main()
