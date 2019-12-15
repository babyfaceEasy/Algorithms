import graph


def main():
    g = graph.Graph()
    g.addEdge(1, 2, 99)
    g.addEdge(1, 3, 50)
    g.addEdge(2, 3, 100)

    g.getAdjacencyMatrix()
    print(g.getAdjacencyList())
    print(g.getEdgeList())


if __name__ == "__main__":
    main()
