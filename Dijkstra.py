import heapq

def dijkstra(graph, start):
    # Distance dictionary with infinity as default
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    
    # Priority queue: (distance, node)
    pq = [(0, start)]
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)

        # Skip if we already found a better path
        if current_dist > dist[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight

            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
     
    return dist

if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4), ('D', 2)],
        'B': [('A', 1), ('D', 5)],
        'C': [('A', 4), ('D', 1)],
        'D': [('A', 2), ('B', 5), ('C', 1)]
    }
    result = dijkstra(graph, 'A')
    print(result)

