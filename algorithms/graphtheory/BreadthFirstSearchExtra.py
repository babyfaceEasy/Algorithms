'''
This algo calculates Breadth First search, node level, parent and the Shortest path
Time Complexity : O(V + E)
'''

from collections import defaultdict


class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, source_vertex, dest_vertex):
        self.graph[source_vertex].append(dest_vertex)

    def getAdjacencyList(self, vertex):
        return self.graph[vertex]

    def addLoneEdge(self, vertex):
        self.graph[vertex] = []

    def getLength(self):
        return len(self.graph.keys())


class BreadthFirstSearchExtra(object):
    def __init__(self, g, start_node):
        self.graph = g
        self.N = g.getLength()
        self.level = {}
        self.parent = {}
        self.start_node = start_node
        self.solver = False

    def bfs_algo(self):
        current_level = 0
        self.level[self.start_node] = current_level
        frontier = [self.start_node]
        while len(frontier) > 0:
            current_node = frontier.pop(0)
            print(current_node, end=" ")
            #current_level += 1
            for node in self.graph.getAdjacencyList(current_node):
                if node not in self.level:
                    self.level[node] = self.level[current_node] + 1
                    self.parent[node] = current_node
                    frontier.append(node)
        self.solver = True
        #print(self.parent)

    def getLevel(self):
        if not self.solver:
            print('Please run the BFS algo first')
        res = defaultdict(list)
        for key, val in sorted(self.level.items()):
            res[val].append(key)
        return res

    def getParent(self):
        if not self.solver:
            print('Please run the BFS algo first')
        res = defaultdict(list)
        for key, val in sorted(self.parent.items()):
            res[val].append(key)
        return res


def main():
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(1, 4)
    g.addEdge(2, 5)
    g.addEdge(2, 6)
    # g.addLoneEdge(3)
    # g.addLoneEdge(4)
    # g.addLoneEdge(5)
    # g.addLoneEdge(6)

    solver = BreadthFirstSearchExtra(g, 0)
    solver.bfs_algo()
    print(solver.getLevel())
    print(solver.getParent())


if __name__ == "__main__":
    main()
