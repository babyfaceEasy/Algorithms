class Graph:

    def __init__(self):
        self.adjancencyList = {}
        self.edgeList = []

        # TODO: work more on the adjacency matrix
        self.width, self.height = 10, 10
        self.adjacencyMatrix = [
            [0 for x in range(self.width)] for y in range(self.height)]

    def addEdge(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

        self.adjancencyList[self.u] = (self.v, self.w)
        self.edgeList.append((self.u, self.v, self.w))
        self.adjacencyMatrix[self.u][self.v] = self.w

    def getAdjacencyMatrix(self):
        for x in range(self.height):
            for y in range(self.width):
                print(self.adjacencyMatrix[x][y], end=' ')
            print()

    def getAdjacencyList(self):
        return self.adjancencyList

    def getEdgeList(self):
        return self.edgeList
