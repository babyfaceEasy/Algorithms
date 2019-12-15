from collections import defaultdict


class Graph:
    def __init__(self):
        self.adjacencyList = defaultdict(list)
        self.count = 0
        # print(self.adjacencyList)

    def addEdge(self, u, v, w):
        if u not in self.adjacencyList.keys():
            self.count += 1
        self.adjacencyList[u].append((v, w))

    def getNode(self, node):
        if node not in self.adjacencyList.keys():
            return []
        return self.adjacencyList[node]

    def getGraph(self):
        return self.adjacencyList



class DepthFirstSearchAdjacencyListRecursive:

    def __init__(self, nodes_count, graph):
        self.graph = graph
        self.nodes_count = nodes_count
        self.visited = [False] * self.nodes_count
        print(self.visited)

    def dfs(self, node):
        if self.visited[node]:
            return

        print(node)
        self.visited[node] = True
        # loop through the adjacency list
        for next_node, weight in self.graph.getNode(node):
            self.dfs(next_node)


def main():
    g = Graph()

    g.addEdge(0, 1, 0)
    g.addEdge(0, 2, 0)
    g.addEdge(1, 3, 0)
    g.addEdge(2, 3, 0)

    print(g.getGraph())

    dfs_obj = DepthFirstSearchAdjacencyListRecursive(4, g)
    dfs_obj.dfs(0)


if __name__ == "__main__":
    main()
