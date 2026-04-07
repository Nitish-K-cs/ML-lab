from queue import PriorityQueue

graph = {
    'A' : [('B' , 4) , ('C' , 3)],
    'B' : [('D' , 5) , ('E' , 12)],
    'C' : [('F' , 7)],
    'D' : [],
    'E' : [('G' , 2)],
    'F' : [],
    'G' : []
    }

herustic = {
    'A' : 10,
    'B' : 8,
    'C' : 5,
    'D' : 7,
    'E' : 3,
    'F' : 6,
    'G' : 0
    }

def bfs(start , goal):
    visited = set()
    pq = PriorityQueue()
    pq.put((herustic[start] , start))
    while not pq.empty():
        h , current = pq.get()
        if current in visited:
            continue
        print(current , end=" ")
        visited.add(current)
        if current == goal:
            print("\nGoal reached")
            return
        for neighbor , cost in graph[current]:
            if neighbor not in visited:
                pq.put((herustic[neighbor] , neighbors))
    print("\nGoal not found")
    
    start_node = 'A'
    goal_node = 'G'
    
    bfs(start_node , goal_node)
        
        
        
        
        
        
        