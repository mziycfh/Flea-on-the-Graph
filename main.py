class Permutation:
    def __init__(self, p):
        self.perm = p

    def __mul__(self, other):
        result = [0, 0, 0]
        for i in range(3):
            result[i] = self.perm[other.perm[i]]
        return Permutation(result)

    def __repr__(self):
        return f"Permutation({self.perm})"

    def left_translate(self, other):
        return other * self

    def right_translate(self, other):
        return self * other


class Graph:
    def __init__(self):
        self.adj_list = {}
        self.vertex_state = {}

    def add_vertex(self, vertex, state):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            self.vertex_state[vertex] = state

    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)

    def get_adjacent_vertices(self, vertex):
        if vertex in self.adj_list:
            return self.adj_list[vertex]
        else:
            return []

    def state_change(self, source, destination):
        self.vertex_state[destination].left_translation(source)

    def __str__(self):
        result = ""
        for vertex in self.adj_list:
            result += str(vertex) + " -> " + str(self.adj_list[vertex]) + " (state: " + str(
                self.vertex_state[vertex]) + ")\n"
        return result


class Flea:
    def __init__(self, position, source, graph):
        self.position = position
        self.source = source
        self.graph = graph

    def hop(self):
        pass


def main():
    graph = Graph()
    initial_states = []
    connection = [[], []]
    for i, state in enumerate(initial_states):
        graph.add_vertex(i, state)
    for i, neighbors in enumerate(connection):
        for neighbor in neighbors:
            graph.add_edge(i, neighbor)

    flea = Flea()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
