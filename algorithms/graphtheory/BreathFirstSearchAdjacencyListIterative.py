'''
Complexity: O(V + E)
'''
from collections import defaultdict
from asyncio import Queue


class Graph:
    def __init__(self):
        self.adjacencyList = defaultdict(list)

    def addEdge(self, u, v):
        self.adjacencyList[u].append(v)

    def getNeighbours(self, u):
        return self.adjacencyList[u]

    def getGraph(self):
        return self.adjacencyList

    def getLength(self):
        return len(self.adjacencyList.keys())


class BreathFirstSearchAdjacencyListIterative:
    def __init__(self, g):
        self.graph = g
        self.visited = [False] * (self.graph.getLength())

    def reconstructPath(self, prev, start_node, end_node):
        path = []
        at = end_node
        while at != None:
            path.append(at)
            at = prev[at]
        path = path[::-1]

        if path[0] == start_node:
            return path
        return []

    def solve(self, start_node):
        prev = [None] * (self.graph.getLength())
        queue = []
        queue.append(start_node)
        #queue = Queue(-1)
        # queue.put(start_node)

        while len(queue) != 0:
            new_node = queue.pop(0)
            for next_node in self.graph.getNeighbours(new_node):
                if self.visited[next_node] == False:
                    self.visited[next_node] = True
                    queue.append(next_node)
                    prev[next_node] = new_node
        return prev

    def bfs(self, start_node, end_node):
        prev = self.solve(start_node)

        return self.reconstructPath(prev, start_node, end_node)


def main():
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(1, 4)
    g.addEdge(2, 6)
    g.addEdge(2, 5)
    g.addEdge(3, 3)
    g.addEdge(4, 4)
    g.addEdge(5, 5)
    g.addEdge(6, 6)

    # print(g.getGraph())

    bfs = BreathFirstSearchAdjacencyListIterative(g)
    print(bfs.bfs(0, 5))


if __name__ == "__main__":
    main()
