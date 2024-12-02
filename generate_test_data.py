import random
import os


# Приведение рёбер к каноническому виду
def normalize_edges(edges):
    return sorted([(min(u, v), max(u, v), w) for u, v, w in edges])


# Функция для записи графа и минимального остова в файл
def write_graph_to_file(filename, mst_edges, graph):
    mst_edges = normalize_edges(mst_edges)
    with open(filename, 'w') as f:
        # Записываем множество рёбер минимального остова
        for edge in mst_edges:
            f.write(f"{edge[0]} {edge[1]} {edge[2]}\n")
        f.write("GRAPH\n")  # Разделитель между MST и графом
        # Записываем сам граф в формате матрицы смежности
        for row in graph:
            f.write(" ".join(map(lambda x: "inf" if x == float('inf') else str(x), row)) + "\n")


# Генерация случайного графа
def generate_random_graph(num_vertices, max_weight=100):
    graph = [[float('inf')] * num_vertices for _ in range(num_vertices)]
    edges = []

    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            weight = random.randint(1, max_weight)
            graph[i][j] = weight
            graph[j][i] = weight
            edges.append((i, j, weight))

    return graph, edges


# Алгоритм Прима для нахождения MST
def find_mst_prim(graph):
    num_vertices = len(graph)
    selected = [False] * num_vertices
    mst_edges = []
    selected[0] = True
    edges = []

    for i in range(num_vertices):
        if graph[0][i] != float('inf'):
            edges.append((graph[0][i], 0, i))  # (вес, вершина1, вершина2)

    edges.sort()

    while len(mst_edges) < num_vertices - 1:
        weight, u, v = edges.pop(0)
        if not selected[v]:
            selected[v] = True
            mst_edges.append((u, v, weight))
            for i in range(num_vertices):
                if graph[v][i] != float('inf') and not selected[i]:
                    edges.append((graph[v][i], v, i))
            edges.sort()

    return mst_edges


# Генерация данных для теста 1
def generate_test_data_random_graphs():
    folder = "test_data_random"
    os.makedirs(folder, exist_ok=True)

    for num_vertices in range(2, 103, 10):
        graph, edges = generate_random_graph(num_vertices)
        mst_edges = find_mst_prim(graph)
        filename = os.path.join(folder, f"graph_{num_vertices}_vertices.txt")
        write_graph_to_file(filename, mst_edges, graph)


# Генерация данных для теста 2 (разное количество компонент связности)
def generate_test_data_connected_components():
    folder = "test_data_components"
    os.makedirs(folder, exist_ok=True)

    num_vertices = 50
    for num_components in range(1, 11):  # Количество компонент связности от 1 до 10
        graph = [[float('inf')] * num_vertices for _ in range(num_vertices)]
        mst_edges = []

        component_size = num_vertices // num_components
        for component in range(num_components):
            start = component * component_size
            end = start + component_size
            if component == num_components - 1:
                end = num_vertices

            subgraph, sub_edges = generate_random_graph(end - start)
            for i in range(end - start):
                for j in range(end - start):
                    graph[start + i][start + j] = subgraph[i][j]
            mst_edges.extend(find_mst_prim(subgraph))

        filename = os.path.join(folder, f"graph_{num_components}_components.txt")
        write_graph_to_file(filename, mst_edges, graph)


# Генерация данных для теста 3 (граф с циклическими зависимостями)
def generate_test_data_cyclic_graphs():
    folder = "test_data_cyclic"
    os.makedirs(folder, exist_ok=True)

    num_vertices = 10
    graph, edges = generate_random_graph(num_vertices)
    for _ in range(5):  # Добавляем дополнительные циклы
        u, v = random.sample(range(num_vertices), 2)
        weight = random.randint(1, 100)
        graph[u][v] = weight
        graph[v][u] = weight
        edges.append((u, v, weight))

    mst_edges = find_mst_prim(graph)
    filename = os.path.join(folder, "cyclic_graph.txt")
    write_graph_to_file(filename, mst_edges, graph)


# Генерация данных для теста 4 (граф с нулевыми весами)
def generate_test_data_zero_weights():
    folder = "test_data_zero_weights"
    os.makedirs(folder, exist_ok=True)

    num_vertices = 10
    graph, edges = generate_random_graph(num_vertices)
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if random.random() < 0.3:  # 30% рёбер имеют нулевой вес
                graph[i][j] = 0
                graph[j][i] = 0

    mst_edges = find_mst_prim(graph)
    filename = os.path.join(folder, "zero_weight_graph.txt")
    write_graph_to_file(filename, mst_edges, graph)
