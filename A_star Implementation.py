class Graph:  # define the data structure of the graph
    def __init__(self, shape):
        self.rows = shape[0]
        self.columns = shape[1]
        self.grid = [[None for i in range(shape[1])] for j in range(shape[0])]
        self.edges = []

    def add_vertex(self, position):
        self.grid[position[0] - 1][position[1] - 1] = position

    def add_edge(self, from_node, to_node, cost):
        self.add_vertex(from_node)
        self.add_vertex(to_node)
        self.edges.append([from_node, to_node, cost])
        self.edges.append([to_node, from_node, cost])

    def get_cost(self, from_node, to_node):
        for i in self.edges:
            if i[0] == from_node and i[1] == to_node:
                return (i[2])

    def get_neighbours(self, position):
        neighbours = []
        for i in self.edges:
            if i[0] == position:
                neighbours.append(i[1])
        return (neighbours)  # define the data structure of the graph#define the data structure of the graph


# creating the given graph
grid = Graph((5, 5))
grid.add_edge((1, 1), (2, 1), 2)
grid.add_edge((2, 1), (3, 1), 3)
grid.add_edge((3, 1), (4, 1), 9)
grid.add_edge((4, 1), (5, 1), 4)
grid.add_edge((1, 2), (2, 2), 1)
grid.add_edge((2, 2), (3, 2), 4)
grid.add_edge((3, 2), (4, 2), 3)
grid.add_edge((4, 2), (5, 2), 1)
grid.add_edge((1, 3), (2, 3), 4)
grid.add_edge((2, 3), (3, 3), 6)
grid.add_edge((3, 3), (4, 3), 4)
grid.add_edge((4, 3), (5, 3), 12)
grid.add_edge((1, 4), (2, 4), 12)
grid.add_edge((2, 4), (3, 4), 15)
grid.add_edge((3, 4), (4, 4), 32)
grid.add_edge((4, 4), (5, 4), 40)
grid.add_edge((1, 5), (2, 5), 1)
grid.add_edge((2, 5), (3, 5), 15)
grid.add_edge((3, 5), (4, 5), 9)
grid.add_edge((4, 5), (5, 5), 4)
grid.add_edge((1, 1), (1, 2), 2)
grid.add_edge((1, 2), (1, 3), 3)
grid.add_edge((1, 3), (1, 4), 15)
grid.add_edge((1, 4), (1, 5), 20)
grid.add_edge((2, 1), (2, 2), 1)
grid.add_edge((2, 2), (2, 3), 5)
grid.add_edge((2, 3), (2, 4), 7)
grid.add_edge((2, 4), (2, 5), 3)
grid.add_edge((3, 1), (3, 2), 2)
grid.add_edge((3, 2), (3, 3), 7)
grid.add_edge((3, 3), (3, 4), 12)
grid.add_edge((3, 4), (3, 5), 10)
grid.add_edge((4, 1), (4, 2), 1)
grid.add_edge((4, 2), (4, 3), 11)
grid.add_edge((4, 3), (4, 4), 31)
grid.add_edge((4, 4), (4, 5), 20)
grid.add_edge((5, 1), (5, 2), 5)
grid.add_edge((5, 2), (5, 3), 15)
grid.add_edge((5, 3), (5, 4), 11)
grid.add_edge((5, 4), (5, 5), 5)
infinity = 10000000000


def a_star(grid, start, end):  # creating the A* algorithm
    def h_function(from_node, to_node):
        return grid.get_cost(from_node, to_node) + abs(to_node[0] - end[0]) + abs(to_node[1] - end[1])

    class card:  # creating a datastructure which stores the value of induvidual vertex
        def __init__(self, position):
            self.name = position
            self.optimal_path = None
            self.path_cost = infinity
            self.cost = infinity

    start_card = card(start)
    start_card.cost = 0
    start_card.path_cost = 0
    start_card.optimal_path = start_card.name
    Queue = [start_card]
    Finished = []

    def init_queue():
        for i in grid.grid:
            for j in i:
                if j != start:
                    c = card(j)
                    Queue.append(c)

    init_queue()

    def merge_sort_by_cost(x):
        n = len(x)
        if n == 1:
            return x
        m = int(n / 2)
        x1 = merge_sort_by_cost(x[:m])
        x2 = merge_sort_by_cost(x[m:])
        return merge(x1, x2)

    def merge(A, B):
        X = []
        while len(A) > 0 and len(B) > 0:
            if A[0].cost > B[0].cost:
                X.append(B[0])
                B.pop(0)
            elif B[0].cost >= A[0].cost:
                X.append(A[0])
                A.pop(0)
        return X + A + B

    def display_queue():
        for i in Queue[:5]:
            print("NAME:", i.name, "TCOST:", i.cost, "path_cost:", i.path_cost, "path:", i.optimal_path)

    current = start_card
    for i in range(24):
        current = Queue[0]
        # print(current.name)
        current_neighbours = grid.get_neighbours(current.name)
        for i in current_neighbours:
            for j in Queue:
                if j.name == i:
                    if h_function(current.name, j.name) + current.path_cost < j.cost:
                        j.cost = h_function(current.name, j.name) + current.path_cost
                    if grid.get_cost(current.name, j.name) + current.path_cost < j.path_cost:
                        j.path_cost = grid.get_cost(current.name, j.name) + current.path_cost
                        j.optimal_path = current.name
        Finished.append(current)
        Queue.pop(0)
        Queue = merge_sort_by_cost(Queue)
        # display_queue()
        # print("_________________________________________")
    Finished.append(Queue[0])
    Queue.pop(0)

    def Optimal_path(Finished):
        optimal_path = [(end)]
        current = end
        while True:
            for i in Finished:
                if i.name == current:
                    optimal_path.append(i.optimal_path)
                    current = i.optimal_path
            if current == start:
                return optimal_path

    opt_path = Optimal_path(Finished)
    opt_path.reverse()
    print(opt_path)


a_star(grid, (2, 2), (5, 5))
