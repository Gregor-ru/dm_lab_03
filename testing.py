import time
import os
from alghoritm import prim_algorithm

# Приведение рёбер к каноническому виду
def normalize_edges(edges):
    return sorted([(min(u, v), max(u, v), w) for u, v, w in edges])

# Функция для чтения графа и минимального остова из файла
def read_graph_from_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    mst_edges = []
    graph = []
    reading_graph = False
    for line in lines:
        line = line.strip()
        if line == "GRAPH":
            reading_graph = True
            continue
        if not reading_graph:
            u, v, weight = map(int, line.split())
            mst_edges.append((u, v, weight))
        else:
            graph.append([float(x) if x != "inf" else float('inf') for x in line.split()])

    return normalize_edges(mst_edges), graph

# Функция для проверки MST
def check_mst(expected_mst, actual_mst):
    return set(map(tuple, expected_mst)) == set(map(tuple, actual_mst))

# Тест 1: Зависимость времени от размера графа
def test_random_graphs():
    folder = "test_data_random"
    results_file = "results_random_graphs.txt"

    # Функция для извлечения количества вершин из имени файла
    def extract_vertices_count(filename):
        # Предположим, что имя файла имеет формат "graph_X.txt", где X - количество вершин
        return int(filename.split('_')[1].split('.')[0])

    # Сортировка файлов по количеству вершин в графе
    with open(results_file, 'w') as results:
        results.write("Размер графа | Время выполнения (секунды)\n")
        results.write("-----------------------------------------\n")

        # Сортировка файлов по количеству вершин, извлечённому из имени файла
        for filename in sorted(os.listdir(folder), key=extract_vertices_count):
            if filename.endswith(".txt"):
                file_path = os.path.join(folder, filename)
                expected_mst, graph = read_graph_from_file(file_path)

                print(f"Тестирование файла: {filename}")
                print("Граф:")
                for row in graph:
                    print(row)

                start_time = time.perf_counter()
                actual_mst = prim_algorithm(graph)
                end_time = time.perf_counter()

                elapsed_time = end_time - start_time
                is_correct = check_mst(expected_mst, actual_mst)

                print("Найденное множество T (минимальный остов):", actual_mst)
                print(f"Результат теста: {'Пройден' if is_correct else 'Ошибка'}")
                print("-" * 50)

                # Запись результатов в файл
                results.write(f"{len(graph)}           | {elapsed_time:.16f} сек |\n")

# Тест 2: Зависимость времени от количества компонент связности
def test_connected_components():
    folder = "test_data_components"
    results_file = "results_connected_components.txt"

    with open(results_file, 'w') as results:
        results.write("Количество компонент | Время выполнения (секунды)\n")
        results.write("---------------------------------------------\n")

        for filename in sorted(os.listdir(folder)):
            if filename.endswith(".txt"):
                file_path = os.path.join(folder, filename)
                expected_mst, graph = read_graph_from_file(file_path)

                print(f"Тестирование файла: {filename}")
                print("Граф:")
                for row in graph:
                    print(row)

                start_time = time.perf_counter()
                actual_mst = prim_algorithm(graph)
                end_time = time.perf_counter()

                elapsed_time = end_time - start_time
                is_correct = check_mst(expected_mst, actual_mst)

                print("Найденное множество T (минимальный остов):", actual_mst)
                print(f"Результат теста: {'Пройден' if is_correct else 'Ошибка'}")
                print("-" * 50)

                results.write(
                    f"{filename.split('_')[1]}               | {elapsed_time:.16f} сек |\n"
                )

# Тест 3: Граф с циклическими зависимостями
def test_cyclic_graphs():
    folder = "test_data_cyclic"
    results_file = "results_cyclic_graphs.txt"

    with open(results_file, 'w') as results:
        results.write("Граф с циклами | Результат\n")
        results.write("--------------------------\n")

        for filename in sorted(os.listdir(folder)):
            if filename.endswith(".txt"):
                file_path = os.path.join(folder, filename)
                expected_mst, graph = read_graph_from_file(file_path)

                actual_mst = prim_algorithm(graph)
                is_correct = check_mst(expected_mst, actual_mst)

                results.write(f"{filename} |\n")


# Тест 4: Граф с нулевыми весами
def test_zero_weights():
    folder = "test_data_zero_weights"
    results_file = "results_zero_weights.txt"

    with open(results_file, 'w') as results:
        results.write("Граф с нулевыми весами | Результат\n")
        results.write("----------------------------------\n")

        for filename in sorted(os.listdir(folder)):
            if filename.endswith(".txt"):
                file_path = os.path.join(folder, filename)
                expected_mst, graph = read_graph_from_file(file_path)

                actual_mst = prim_algorithm(graph)
                is_correct = check_mst(expected_mst, actual_mst)

                results.write(f"{filename} | {'Пройден' if is_correct else 'Ошибка'}\n")

