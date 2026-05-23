import heapq

def dijkstra(graph, start):
    INF = float('inf')

    n = len(graph)

    distances = [INF] * n
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:

            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


vertices = 7

graph = [[] for _ in range(vertices)]


def add_edge(u, v, w):
    graph[u].append((v, w))
    graph[v].append((u, w))

add_edge(0, 1, 4)
add_edge(0, 2, 3)
add_edge(1, 3, 2)
add_edge(1, 4, 7)
add_edge(2, 4, 4)
add_edge(3, 5, 1)
add_edge(4, 5, 3)
add_edge(4, 6, 5)
add_edge(5, 6, 7)

start_vertex = 3

shortest_paths = dijkstra(graph, start_vertex)

print(f"Найкоротші шляхи від вершини {start_vertex}:")

for vertex, distance in enumerate(shortest_paths):
    print(f"До вершини {vertex}: {distance}")