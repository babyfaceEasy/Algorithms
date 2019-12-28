'''
An implementation of Tarjan's Strongly connected algorithm uisng an adjacency list.

Time complexity : O(V+E)

@author Olakunle, Odegbaro oodegbaro@gmail.com
'''

from collections import defaultdict


class Graph(object):
    def __init__(self):
        self.adjacencyList = defaultdict(list)

    def addEdge(self, vertex_from, vertex_to, edge_cost):
        self.adjacencyList[vertex_from].append((vertex_to, edge_cost))

    def getEdges(self, vertex):
        return self.adjacencyList[vertex]

    def getLength(self):
        return len(self.adjacencyList.keys())


class TarjanSccSolverAdjacencyList(object):
    UNVISITED = -1

    def __init__(self, g):
        self.graph = g
        self.N = g.getLength()
        self.id = 0
        self.SccsCount = 0
        self.ids = [self.UNVISITED] * (self.N)
        self.low = [0] * (self.N)
        self.onStack = [False] * (self.N)
        self.stack = []

    def getTotalComponents(self):
        return self.SccsCount

    def findSccs(self):
        # self.ids = [self.UNVISITED] * (self.N)
        counter = 0
        while counter < self.N:
            if self.ids[counter] == self.UNVISITED:
                self.dfs(counter)
            counter += 1
        print(self.SccsCount)
        return self.low

    def dfs(self, at):
        self.stack.append(at)
        self.onStack[at] = True
        self.id += 1
        self.ids[at] = self.low[at] = self.id

        # visit all neighbours and min low-link on callback
        for vertex_to, edge_cost in self.graph.getEdges(at):
            if self.ids[vertex_to] == self.UNVISITED:
                self.dfs(vertex_to)

            if self.onStack[vertex_to]:
                self.low[at] = min(self.low[at], self.low[vertex_to])

        # after having visited all the neighbours of `at`
        # if we at the start of a SCC empty the seen stack until we are back to the start
        # of the SCC
        if self.ids[at] == self.low[at]:
            node = self.stack.pop()
            while node != None:
                self.onStack[node] = False
                self.low[node] = self.ids[at]
                if node == at:
                    break
                self.SccsCount += 1
                node = self.stack.pop()


def main():
    g = Graph()
    g.addEdge(0, 1, 0)
    g.addEdge(1, 0, 0)
    g.addEdge(2, 0, 0)
    g.addEdge(2, 3, 0)
    g.addEdge(3, 4, 0)
    g.addEdge(4, 2, 0)
    g.addEdge(4, 0, 0)
    g.addEdge(4, 5, 0)
    g.addEdge(5, 1, 0)

    sccs = TarjanSccSolverAdjacencyList(g)
    print(sccs.findSccs())


if __name__ == "__main__":
    main()
