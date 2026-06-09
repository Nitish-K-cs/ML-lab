from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}


def bfs(start, goal):

    visited = set()
    queue = deque([start])

    while queue:

        current = queue.popleft()

        if current in visited:
            continue

        print(current, end=" ")

        visited.add(current)

        if current == goal:
            print("\nGoal Reached")
            return

        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)

    print("\nGoal Not Found")


bfs('A', 'G')

#A B C D E F G 
#Goal Reached
