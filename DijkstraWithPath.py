
import heapq

def dijkstra_with_path(graph, start):
    # Distance from start to each node
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

# Previous node (for path reconstruction)
    prev = {node: None for node in graph}

    # Priority queue (min-heap)
    pq = [(0, start)]

    while pq:
        current_dist, u = heapq.heappop(pq)

        if current_dist > dist[u]:
            continue

        for v, weight in graph[u]:
            new_dist = current_dist + weight
	    
            if new_dist < dist[v]:
                dist[v] = new_dist
                prev[v] = u
                heapq.heappush(pq, (new_dist, v))

    return dist, prev
	

def get_path(prev, start, end):
    path = []
    node = end

    while node is not None:
        path.append(node)
        node = prev[node]

    path.reverse()

    if path[0] == start:
        return path
    else:
        return None  # No path

if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('D', 4)],
        'B': [('A', 1), ('C', 2), ('E', 5)],
        'C': [('B', 2)],
        'D': [('A', 4), ('E', 1)],
        'E': [('D', 1), ('B', 5)]
    }


    dist, prev = dijkstra_with_path(graph, 'A')

    for node in graph:
        path = get_path(prev, 'A', node)
        print(f"A → {node}: distance = {dist[node]}, path = {path}")