'''
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


class ArticulationPointsEdgeList(object):
    def __init__(self, g):
        self.graph = g
        self.N = g.getLength()
        self.id = 0
        self.ids = [0] * (self.N)
        self.low = [0] * (self.N)
        self.visited = [False] * (self.N)
        self.is_art = [False] * (self.N)
        self.outEdgeCount = 0

    def findArtPoints(self):
        counter = 0
        while counter < self.N:
            if not self.visited[counter]:
                self.outEdgeCount = 0
                self.dfs(counter, counter, -1)
                self.is_art[counter] = (self.outEdgeCount > 1)
            counter += 1
        return self.is_art

    def dfs(self, root, at, parent):
        if parent == root:
            self.outEdgeCount += 1
        self.visited[at] = True
        self.id += 1
        self.low[at] = self.ids[at] = self.id

        for to in self.graph.getEdges(at):
            to_node, edge_cost = to
            if to_node == parent:
                continue
            if not self.visited[to_node]:
                self.dfs(root, to_node, at)
                self.low[at] = min(self.low[at], self.low[to_node])
                # articulation point found via bridge
                if self.ids[at] < self.low[to_node]:
                    self.is_art[at] = True
                # articulation found via cycle
                if self.ids[at] == self.low[to_node]:
                    self.is_art[at] = True
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

    artPoint = ArticulationPointsEdgeList(g)
    print(artPoint.findArtPoints())


if __name__ == "__main__":
    main()
