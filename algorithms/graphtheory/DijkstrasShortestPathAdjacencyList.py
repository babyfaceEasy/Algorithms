'''
This file contains an implementation of Dijkstra's shortest path algorithm from a start node to a
specific ending node. Dijkstra can also be modified to find the shortest path between a starting
node and all other nodes in the graph. However, in this implementation since we're only going
from a starting node to an ending node we can employ an optimization to stop early once we've
visited all the neighbors of the ending node.

@author Olakunle Odegbaro, oodegbaro@gmail.com
'''

from collections import defaultdict
from queue import PriorityQueue
import math


class Graph(object):
    def __init__(self):
        self.adjacencyList = defaultdict(list)

    def addEdge(self, from_vertex, to_vertex, edge_cost):
        self.adjacencyList[from_vertex].append((to_vertex, edge_cost))

    def getEdges(self, vertex):
        return self.adjacencyList[vertex]

    def getLength(self):
        return len(self.adjacencyList.keys())


class DijkstrasShortestPathAdjacencyList(object):
    def __init__(self, g):
        self.graph = g
        self.no_nodes = self.graph.getLength()

    def printPQ(self, pq):
        print(pq.queue)

    def ssps(self, start_node):
        visited = [False] * (self.no_nodes)
        dist = [math.inf] * (self.no_nodes)
        prev = [None] * (self.no_nodes)
        pq = PriorityQueue()

        # set initial values
        dist[start_node] = 0
        # format = (dist, node_index) this is because we need the dist to b our priority
        pq.put((0, start_node))

        # loop while pq not empty
        while not pq.empty():
            # self.printPQ(pq)
            min_value, node_index = pq.get()
            # self.printPQ(pq)
            visited[node_index] = True
            if dist[node_index] < min_value:
                continue
            for edge in self.graph.getEdges(node_index):
                vertex_to, edge_cost = edge
                if visited[vertex_to]:
                    continue
                new_dist = dist[node_index] + edge_cost
                if new_dist < dist[vertex_to]:
                    prev[vertex_to] = node_index
                    dist[vertex_to] = new_dist
                    pq.put((new_dist, vertex_to))
        return (dist, prev)

    def findShortestPath(self, start_node, end_node):
        dist, prev = self.ssps(start_node)
        path = []
        if (dist[end_node] == math.inf):
            return path
        at = end_node
        while at != None:
            path.append(at)
            at = prev[at]
        path = path[::-1]
        return path


def main():
    g = Graph()
    g.addEdge(0, 1, 4)
    g.addEdge(0, 2, 1)
    g.addEdge(1, 3, 1)
    g.addEdge(2, 1, 2)
    g.addEdge(2, 3, 5)
    g.addEdge(3, 4, 3)
    g.addEdge(4, 4, 0)

    djikstra = DijkstrasShortestPathAdjacencyList(g)
    print(djikstra.ssps(0)[0])
    print(djikstra.findShortestPath(0, 1))


if __name__ == "__main__":
    main()
