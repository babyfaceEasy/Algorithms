'''
An implementation of the lazy version of Prim's algorithm which relies on using a traditional
priority queue to query the next best edge.

Time Complexity : O(ELogE)

@uthor Olakunle Odegbaro, oodegbaro@gmail.com
'''
from collections import defaultdict
from queue import PriorityQueue


class Graph(object):
    def __init__(self):
        self.adjacencyList = defaultdict(list)

    def addEdge(self, from_vertex, to_vertex, edge_cost):
        self.adjacencyList[from_vertex].append((to_vertex, edge_cost))
        self.adjacencyList[to_vertex].append((from_vertex, edge_cost))

    def addSingleNode(self, vertex):
        self.adjacencyList[vertex] = []

    def getLength(self):
        return len(self.adjacencyList.keys())

    def getOutEdges(self, vertex):
        return self.adjacencyList[vertex]


class LazyPrimsAdjacencyList(object):
    def __init__(self, g):
        self.g = g
        self.N = g.getLength()
        self.visited = [False] * (self.N)
        self.pq = PriorityQueue()  # (priorit_number, data)

    def addEges(self, node_index):
        # mark the current node as visited
        self.visited[node_index] = True

        # iterate over all the out going edges from the current node
        # add edges to the PQ which point to the unvisited node
        edges = self.g.getOutEdges(node_index)
        for edge in edges:
            # unpack edge
            edge_to, edge_cost = edge
            if not self.visited[edge_to]:
                pq_data = (edge_cost, (node_index, edge_to, edge_cost))
                self.pq.put(pq_data)

    def lazyPrimsAlgo(self, start_node):
        no_edges = self.N - 1  # number of edges in MST
        edgeCount, mstCost = 0, 0
        mstEdges = [None] * (no_edges)

        self.addEges(start_node)

        while not self.pq.empty() and edgeCount != no_edges:
            edge = self.pq.get()
            # print(edge)
            # unpack the tuple
            edge_from, edge_to, edge_cost = edge[1]
            if self.visited[edge_to]:
                continue
            mstEdges[edgeCount] = edge_to
            edgeCount += 1
            print(edge_cost)
            mstCost += edge_cost

            self.addEges(edge_to)

        if edgeCount != no_edges:
            return (None, None)  # no MST exists
        return (mstCost, mstEdges)


def main():
    g = Graph()
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 1)
    g.addEdge(0, 3, 4)
    g.addEdge(1, 4, 0)
    g.addEdge(1, 2, 3)
    g.addEdge(2, 5, 8)
    g.addEdge(2, 3, 2)
    g.addEdge(3, 5, 2)
    g.addEdge(3, 6, 7)
    g.addEdge(4, 7, 8)
    g.addEdge(4, 5, 1)
    g.addEdge(5, 7, 9)
    g.addEdge(5, 6, 6)
    g.addEdge(6, 7, 12)
    g.addSingleNode(7)

    mstSolver = LazyPrimsAdjacencyList(g)
    print(mstSolver.lazyPrimsAlgo(0))


if __name__ == '__main__':
    main()
