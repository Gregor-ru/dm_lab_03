import heapq

def prim_algorithm(graph):
    num_vertices = len(graph)
    # Для хранения минимального остова
    T = []

    # Массивы для хранения минимальных расстояний
    beta = [float('inf')] * num_vertices
    alpha = [-1] * num_vertices
    beta[0] = 0  # Начинаем с первой вершины

    min_heap = [(0, 0)]  # (расстояние, вершина)

    visited = [False] * num_vertices

    while min_heap:
        # Извлекаем вершину с минимальным расстоянием
        dist, u = heapq.heappop(min_heap)

        if visited[u]:
            continue
        visited[u] = True

        # Добавляем ребро в минимальный остов
        if alpha[u] != -1:
            # Приводим ребро к каноническому виду
            edge = (min(alpha[u], u), max(alpha[u], u), graph[u][alpha[u]])
            T.append(edge)

        # Обновляем расстояния до соседей
        for v in range(num_vertices):
            if not visited[v] and graph[u][v] < beta[v]:
                beta[v] = graph[u][v]
                alpha[v] = u
                heapq.heappush(min_heap, (beta[v], v))

    return T

"""
# Пример использования
graph = [
    [float('inf'), 2, float('inf'), 6, float('inf')],
    [2, float('inf'), 3, 8, 5],
    [float('inf'), 3, float('inf'), float('inf'), 7],
    [6, 8, float('inf'), float('inf'), 9],
    [float('inf'), 5, 7, 9, float('inf')]
]

mst = prim_algorithm(graph)
print("Минимальный остов:")
for edge in mst:
    print(f"Ребро: {edge[0]} - {edge[1]}, вес: {edge[2]}")
"""
