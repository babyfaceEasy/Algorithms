'''
An implementation of the Bellman-Ford algorithm. The algorithm finds the shortest path between a
starting node and all other nodes in the graph. The algorithm also detects negative cycles.
Time Complexity : 0(VE)

@author Olakunle Odegbaro, oodegbaro@gmail.com
'''

from collections import defaultdict
from math import inf


class Graph(object):
    def __init__(self):
        self.adjacencyList = defaultdict(list)

    def addEdge(self, u, v, w):
        self.adjacencyList[u].append((v, w))

    def getEdges(self):
        return self.adjacencyList[u]

    def getLength(self):
        return len(self.adjacencyList.keys())


class BellmanForsAdjacencyList(object):
    def __init__(self, g):
        self.g = g
        self.no_of_nodes = g.getLength()
        self.dist = [inf] * (self.no_of_nodes)

    def bf_algo(self, start_node):
        self.dist[start_node] = 0
        counter = 0

        while counter < self.no_of_nodes - 1:
            visited = [False] * (self.no_of_nodes)
            counter += 1


def main():
    pass


if __name__ == "__main__":
    main()
