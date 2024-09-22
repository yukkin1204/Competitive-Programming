import heapq
from sys import stdin

def dijkstra(graph, start, end):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node == end:
            return distances[end]

        if distances[current_node] < current_distance:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return None

N = int(input())
l = [list(map(int, stdin.readline().split())) for _ in range(N - 1)]
d = dict()

for i in range(N - 1):
    A, B, X = l[i][0], l[i][1], l[i][2]
    if i + 2 == X:
        d[i + 1] = {X: min(A, B)}
    else:
        d[i + 1] = {i + 2: A, X: B}
d[N] = {}

print(dijkstra(d, 1, N))