import heapq


def dijkstra(graph, start):
    distances = {vertex: float("inf") for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]  # Купа: (відстань, вершина)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue  # Пропускаємо, якщо знайдений довший шлях

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Граф міст та відстаней
graph = {
    "New York": {"Boston": 215, "Chicago": 790, "Houston": 1620, "Miami": 1280},
    "Boston": {"New York": 215, "Chicago": 980},
    "Chicago": {"New York": 790, "Boston": 980, "Houston": 940, "Miami": 1380},
    "Houston": {"New York": 1620, "Chicago": 940, "Miami": 1180},
    "Miami": {"New York": 1280, "Houston": 1180, "Chicago": 1380},
}

# Обчислення найкоротших шляхів між всіма містами
all_shortest_paths = {vertex: dijkstra(graph, vertex) for vertex in graph}

# Вивід результатів у вигляді таблиці
print("\nShortest connections between cities\n")
print(f"{'From/To':<12} {'  '.join(graph.keys()):<50}")
print("-" * 62)
for start, distances in all_shortest_paths.items():
    row = f"{start:<15} "
    row += "  ".join(f"{distances[dest]:<5}" for dest in graph.keys())
    print(row)
