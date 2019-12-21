'''
An implementation of the Bellman-Ford algorithm. The algorithm finds the shortest path between a
starting node and all other nodes in the graph. The algorithm also detects negative cycles.

Time Complexity : 0(VE)

@author Olakunle Odegbaro, oodegbaro@gmail.com
'''

from math import inf


class Graph(object):
    def __init__(self):
        self.graph = []

    def addEdge(self, vertex_from, vertex_to, edge_cost):
        self.graph.append((vertex_from, vertex_to, edge_cost))

    def getEdges(self):
        return self.graph

    def getLength(self):
        pass


class BellmanFordEdgeList(object):

    def __init__(self, g, no_of_nodes):
        self.graph = g
        self.N = no_of_nodes
        self.dist = [inf] * (self.N)
        print(self.dist)

    def bf_algos(self, start_node):
        self.dist[start_node] = 0

        counter = 0
        while counter < self.N:
            for edge_from, edge_to, edge_cost in self.graph.getEdges():
                # relax the edges and update the dist array
                if self.dist[edge_from] + edge_cost < self.dist[edge_to]:
                    self.dist[edge_to] = self.dist[edge_from] + edge_cost
            counter += 1

        # reapeat to find nodes caught in a negative cycle
        counter = 0
        while counter < self.N:
            for edge_from, edge_to, edge_cost in self.graph.getEdges():
                if self.dist[edge_from] + edge_cost < self.dist[edge_to]:
                    self.dist[edge_to] = float('-inf')
            counter += 1
        return self.dist


def main():
    g = Graph()
    g.addEdge(0, 1, 5)
    g.addEdge(1, 6, 60)
    g.addEdge(1, 2, 20)
    g.addEdge(1, 5, 30)
    g.addEdge(2, 3, 10)
    g.addEdge(2, 4, 75)
    g.addEdge(3, 2, -15)
    g.addEdge(5, 6, 5)

    bf = BellmanFordEdgeList(g, 7)
    print(bf.bf_algos(0))


if __name__ == "__main__":
    main()
