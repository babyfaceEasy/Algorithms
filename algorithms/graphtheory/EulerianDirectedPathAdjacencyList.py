'''
Implementation of finding an Eulerian Path on a graph. This implementation 
verifies that the input graph is fully connected and supports self loop and 
repeated edges between nodes.

Time Complexity :  O(E)

@author Olakunle Odegbaro, oodegbaro@gmail.com
'''

from collections import defaultdict


class Graph(object):
    def __init__(self):
        self.adjacencyList = defaultdict(list)
        self.edgeList = []
        self.edgesCount = 0

    def addSingleNode(self, u):
        self.adjacencyList[u]

    def addEdge(self, u, v, w):
        self.adjacencyList[u].append((v, w))
        self.edgeList.append((u, v, w))
        self.edgesCount += 1

    def getLength(self):
        return len(self.adjacencyList.keys())

    def getEdges(self, u):
        return self.adjacencyList[u]

    def getEdgesCount(self):
        return self.edgesCount

    def getGraphEdges(self):
        return self.edgeList


class EulerianDirectedPathAdjacencyList(object):
    def __init__(self, g):
        self.graph = g
        self.M = self.graph.getEdgesCount()
        self.N = self.graph.getLength()
        self.in_degrees = [0] * self.N
        self.out_degrees = [0] * self.N
        self.path = []

    def countInOutDegrees(self):
        for node_from, node_to, weight in self.graph.getGraphEdges():
            self.out_degrees[node_from] += 1
            self.in_degrees[node_to] += 1

    def graphHasEulerianPath(self):
        start_node, end_node = 0, 0
        i = 0
        while i < self.N:
            if self.out_degrees[i] - self.in_degrees[i] > 1 or self.in_degrees[i] - self.out_degrees[i] > 1:
                return False
            elif self.out_degrees[i] - self.in_degrees[i] == 1:
                start_node += 1
            elif self.in_degrees[i] - self.out_degrees[i] == 1:
                end_node += 1
            i += 1
        return (end_node == 0 and start_node == 0) or (end_node == 1 and start_node == 1)

    def findStartNode(self):
        start = 0
        for i in range(0, self.N):
            # unique starting node:
            if self.out_degrees[i] - self.in_degrees[i] == 1:
                return i
            # start at any node with an outgoing edge
            if self.out_degrees[i] > 0:
                start = i
        return start

    def dfs(self, at):
        # while the current node still has outgoing edges
        while self.out_degrees[at]:
            # select the next unvisited outgoing edge
            self.out_degrees[at] -= 1
            next_edge_to, weight = self.graph.getEdges(
                at)[self.out_degrees[at]]
            self.dfs(next_edge_to)
        # add current node to solution
        self.path.insert(0, at)

    def findEulerianPath(self):
        self.countInOutDegrees()
        print(self.graphHasEulerianPath())
        if not self.graphHasEulerianPath():
            return None
        self.dfs(self.findStartNode())

        # return eulerian path if we traversed all the edges. The graph might be
        # disconnected, in which case its impossible to have an euler path.
        if len(self.path) == self.M + 1:
            return self.path
        print(self.graph.getEdgesCount())
        return None


def main():
    g = Graph()
    g.addEdge(0, 1, 0)
    g.addEdge(1, 2, 0)
    g.addEdge(1, 3, 0)
    g.addEdge(2, 1, 0)
    g.addEdge(3, 4, 0)
    g.addSingleNode(4)

    eulerianSolver = EulerianDirectedPathAdjacencyList(g)
    print(eulerianSolver.findEulerianPath())

    g = Graph()
    g.addEdge(0, 1, 0)
    g.addEdge(0, 1, 0)
    g.addEdge(1, 2, 0)
    g.addEdge(2, 0, 0)
    g.addEdge(1, 3, 0)
    g.addEdge(3, 0, 0)

    eulerianSolver = EulerianDirectedPathAdjacencyList(g)
    print(eulerianSolver.findEulerianPath())

    g = Graph()
    g.addSingleNode(0)
    g.addEdge(1, 2, 0)
    g.addEdge(1, 3, 0)
    g.addEdge(2, 2, 0)
    g.addEdge(2, 4, 0)
    g.addEdge(2, 4, 0)
    g.addEdge(3, 1, 0)
    g.addEdge(3, 2, 0)
    g.addEdge(3, 5, 0)
    g.addEdge(4, 3, 0)
    g.addEdge(4, 6, 0)
    g.addEdge(6, 3, 0)
    g.addEdge(5, 6, 0)

    eulerianSolver = EulerianDirectedPathAdjacencyList(g)
    print(eulerianSolver.findEulerianPath())


if __name__ == "__main__":
    main()
