Graph_nodes = {
    'A': [('B', 6), ('F', 3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 8)],
    'E': [('I', 5), ('J', 5)],
    'F': [('G', 1), ('H', 7)],
    'G': [('I', 3)],
    'H': [('I', 2)],
    'I': [('E', 5), ('J', 3)]
}

heuristic = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 6,
    'G': 5,
    'H': 3,
    'I': 1,
    'J': 0
}


def astar(graph, heuristic, start, goal):

    open_list = [(start, 0)]      # (node, g_cost)
    parent = {start: None}
    cost = {start: 0}

    while open_list:

        current = min(
            open_list,
            key=lambda x: x[1] + heuristic[x[0]]
        )[0]

        if current == goal:

            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            return path

        open_list = [
            item for item in open_list
            if item[0] != current
        ]

        for neighbor, weight in graph.get(current, []):

            new_cost = cost[current] + weight

            if neighbor not in cost or new_cost < cost[neighbor]:

                cost[neighbor] = new_cost
                parent[neighbor] = current

                open_list.append(
                    (neighbor, new_cost)
                )

    return None


start = 'A'
goal = 'J'

path = astar(
    Graph_nodes,
    heuristic,
    start,
    goal
)

print("Path Found:", path)
#Output
#Path Found: ['A', 'F', 'G', 'I', 'J']
