# Импортируем необходимые модули
import generate_test_data
import alghoritm

from testing import (
    test_random_graphs,
    test_connected_components,
    test_cyclic_graphs,
    test_zero_weights
)

def generate_test():
    generate_test_data.generate_test_data_random_graphs()
    generate_test_data.generate_test_data_connected_components()
    generate_test_data.generate_test_data_cyclic_graphs()
    generate_test_data.generate_test_data_zero_weights()

def run_tests():
    print("Запуск тестов...")

    print("1. Тест: Зависимость времени от размера графа.")
    test_random_graphs()
    print("Результаты записаны в results_random_graphs.txt")

    print("2. Тест: Зависимость времени от количества компонент связности.")
    test_connected_components()
    print("Результаты записаны в results_connected_components.txt")

    print("3. Тест: Граф с циклическими зависимостями.")
    test_cyclic_graphs()
    print("Результаты записаны в results_cyclic_graphs.txt")

    print("4. Тест: Граф с нулевыми весами.")
    test_zero_weights()
    print("Результаты записаны в results_zero_weights.txt")

    print("Все тесты завершены.")

def main():
    #generate_test()
    run_tests()

    print("Все тесты завершены.")


if __name__ == "__main__":
    main()
