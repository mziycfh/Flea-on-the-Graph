class Permutation:
    def __init__(self, p):
        self.perm = p
        self.length = len(p)

    def __mul__(self, other):
        assert (self.length == len(other))
        result = [0] * self.length
        for i in range(self.length):
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
        self.state_list = {}

    def __str__(self):
        result = ""
        for vertex in self.adj_list:
            result += str(vertex) + " -> " + str(self.adj_list[vertex]) + " (state: " + str(
                self.state_list[vertex]) + ")\n"
        return result

    def add_vertex(self, vertex, state):
        """
        :param vertex: index of the vertex
        :param state: the state of the corresponding vertex (a Permutation)
        :return: none
        """
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            self.state_list[vertex] = state

    def add_edge(self, v1, v2):
        """
        :param v1: index of the first vertex the edge is incident to
        :param v2: index of the second vertex the edge is incident to
        :return: none
        """
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
        else:
            print("add_edge failed: vertex not found")

    def state_change(self, position, destination):
        """
        :param position: index of the current vertex
        :param destination: index of the destination vertex
        :return: none
        """
        self.state_list[destination].left_translation(self.state_list[position])


class Flea:
    def __init__(self, position, source, graph, trace):
        """
        :param position: index of the vertex the flea is currently on
        :param source: the index of the vertex the flea comes from
        :param graph: the graph the flea is on
        :param trace: the trace of the flea
        """
        self.position = position
        self.source = source
        self.graph = graph
        self.trace = [position]

    def hop(self):
        current_state = self.graph.state_list[self.position]
        destination = current_state[self.source]
        self.graph.state_change(position=self.position, destination=destination)
        self.source = self.position
        self.position = destination
        self.trace.append(self.position)


def main():
    graph = Graph()
    initial_states = [[], []]
    for i, state in enumerate(initial_states):
        graph.add_vertex(i, state)
    edges = [(), ]
    for i, edge in enumerate(edges):
        graph.add_edge(edge[0], edge[1])
    flea = Flea()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
