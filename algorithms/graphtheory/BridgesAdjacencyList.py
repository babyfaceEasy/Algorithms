'''

Time Complexity : 0(V+E)

@author Olakunle Odegbaro, oodegbaro@gmail.com
'''

from collections import defaultdict


class Graph(object):
    def __init__(self):
        self.adjacencyList = defaultdict(list)

    def addEdge(self, u, v, w):
        self.adjacencyList[u].append((v, w))

    def getLength(self):
        return len(self.adjacencyList.keys())

    def getEdges(self, u):
        return self.adjacencyList[u]


class BridgesAdjacencyList(object):
    def __init__(self, g):
        self.graph = g
        self.N = g.getLength()
        self.id = 0
        self.ids = [0] * (self.N)
        self.low = [0] * (self.N)
        self.visited = [False] * (self.N)

    def findBridges(self):
        bridges = []
        # find all bridges in the graph across various connected components
        counter = 0
        while counter < self.N:
            if not self.visited[counter]:
                self.dfs(counter, -1, bridges)
            counter += 1
        return bridges

    def dfs(self, at, parent, bridges):
        self.visited[at] = True
        self.id += 1
        self.low[at] = self.ids[at] = self.id

        # go through each node from `at` to `to` node
        for to in self.graph.getEdges(at):
            to_node, edge_cost = to
            if to_node == parent:
                continue
            if not self.visited[to_node]:
                self.dfs(to_node, at, bridges)
                self.low[at] = min(self.low[at], self.low[to_node])
                if self.ids[at] < self.low[to_node]:
                    bridge = (at, to_node)
                    bridges.append(bridge)
                    # bridges.append(to[0])
            else:
                self.low[at] = min(self.low[at], self.ids[to_node])


def main():
    g = Graph()
    g.addEdge(0, 1, 0)
    g.addEdge(1, 2, 0)
    g.addEdge(2, 0, 0)
    g.addEdge(2, 5, 0)
    g.addEdge(2, 3, 0)
    g.addEdge(3, 4, 0)
    g.addEdge(4, 4, 0)
    g.addEdge(5, 6, 0)
    g.addEdge(6, 7, 0)
    g.addEdge(7, 8, 0)
    g.addEdge(8, 5, 0)

    bridgeClass = BridgesAdjacencyList(g)
    print(bridgeClass.findBridges())


if __name__ == "__main__":
    main()
