def dijkstra(graph, start):
    # Initialize the distance dictionary with all nodes except the start node set to infinity
    # and the start node set to 0
    distance = {node: float('inf') for node in graph}
    distance[start] = 0

    # Create a set of unvisited nodes
    unvisited = set(graph)

    while unvisited:
        # Find the node in the unvisited set with the smallest distance
        current_node = min(unvisited, key=lambda node: distance[node])

        # Remove the current node from the unvisited set
        unvisited.remove(current_node)

        # Update the distances for all neighboring nodes of the current node
        for neighbor, weight in graph[current_node].items():
            # Calculate the tentative distance to the neighbor through the current node
            tentative_distance = distance[current_node] + weight

            # If the tentative distance is less than the current distance to the neighbor,
            # update the distance dictionary with the new value
            if tentative_distance < distance[neighbor]:
                distance[neighbor] = tentative_distance
                
                # Add the neighbor back to the unvisited set
                unvisited.add(neighbor)

    return distance
    
    
graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'D': 3, 'E': 2},
    'C': {'B': 1, 'F': 4},
    'D': {'E': 1, 'G': 3},
    'E': {'H': 2},
    'F': {'G': 2, 'H': 1},
    'G': {'E': 1, 'H': 2},
    'H': {}
}

start_node = 'A'

distances = dijkstra(graph, start_node)

print(distances)