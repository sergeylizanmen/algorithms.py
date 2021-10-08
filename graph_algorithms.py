from collections import deque
from typing import Any
from general import timer

""" Алгоритмы для графов """


@timer
def go_wide_birds_eye_view(graph: dict, start: Any) -> Any | None:
    """
    Поиск в ширину по графу BFS - работает с невзвешенными графами
    Находит кратчайший путь по количеству узлов

    Ищет ближайшее имя из 5 букв
    Иначе возвращает None

    Время выполнения O(V+E)
    V-количество вершин
    E-количество ребер
    """
    search_queue = deque()  # Создаем Очередь
    search_queue.extend(graph[start])

    checked_list = []  # Проверенные
    while search_queue:
        name = search_queue.popleft()

        if name not in checked_list:
            if len(name) == 5:
                return name

            # Если узел не соответсвует условию, добавляем его соседов в конец очереди
            checked_list.append(name)
            search_queue.extend(graph[name])
    return None


@timer
def go_deep_head_first(graph: dict, start: Any) -> Any | None:
    """
    Поиск в глубину по графу DFS - работает с невзвешенными графами
    Работает в некоторых случаях быстрее BFS и находит любой путь

    Ищет ближайшее имя из 5 букв
    Иначе возвращает None

    Время выполнения O(V+E)
    V-количество вершин
    E-количество ребер
    """
    search_queue = deque()  # Создаем Очередь
    search_queue.extend(graph[start])

    checked_list = []  # Проверенные
    while search_queue:
        name = search_queue.popleft()

        if name not in checked_list:
            if len(name) == 5:
                return name

            # Если узел не соответсвует условию, добавляем его соседов в начало очереди
            checked_list.append(name)
            search_queue.extendleft(graph[name])
    return None


@timer
def Dijkstras_algorithm(graph: dict, start: Any, finish: Any) -> int | None:
    """
    Алгоритм Дейкстры
    Позволяет найти кратчайшие пути для каждого узла во взвешенном графе
    При условии, что в нем нет отрицательных значений

    Время выполнения O(n * log2 n + Е)
    E-количество ребер
    """

    def find_lowest_cost_node():
        lowest_cost = float("inf")
        lowest_cost_node = None
        for node_key in costs:
            if costs[node_key] < lowest_cost and node_key not in checked_list:
                lowest_cost = costs[node_key]
                lowest_cost_node = node_key
        return lowest_cost_node

    # Таблица стоимостей
    costs = graph[start]

    checked_list = []  # Проверенные

    current_node = find_lowest_cost_node()  # Текущий узел

    while current_node:
        cost = costs[current_node]
        neighbors = graph[current_node]  # Его соседи

        for node in neighbors.keys():
            try:
                if costs[node] > cost + neighbors[node]:
                    costs[node] = cost + neighbors[node]
            except KeyError:
                costs[node] = cost + neighbors[node]

        checked_list.append(current_node)
        if finish in checked_list:
            break
        current_node = find_lowest_cost_node()

    return costs[finish]


if __name__ == '__main__':
    # Невзвешенный граф (на картинке unweighted_graph.jpg)
    unweighted_graph = {
        'you': ['bob', 'alice', 'claire'],
        'bob': ['anudzh', 'peggy'],
        'alice': ['peggy'],
        'claire': ['tom', 'jonny'],
        'anuj': [],
        'peggy': [],
        'tom': [],
        'jonny': []
    }
    print('Поиск в ширину (имя из 5 букв):', go_wide_birds_eye_view(unweighted_graph, 'you'))
    print('Поиск в глубину (имя из 5 букв):', go_deep_head_first(unweighted_graph, 'you'))

    # Ввзвешенный граф (на картинке weighted_graph.jpg)

    weighted_graph = {
        'start': {'a': 5, 'b': 2},
        'a': {'c': 4, 'd': 2},
        'b': {'a': 8, 'd': 7},
        'c': {'finish': 3, 'd': 6},
        'd': {'finish': 1},
        'finish': {}
    }
    print('Алгоритм Дейкстры (кратчайший путь из старт в финиш):',
          Dijkstras_algorithm(weighted_graph, 'start', 'finish'))
