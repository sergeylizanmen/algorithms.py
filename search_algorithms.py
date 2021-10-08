from typing import Any
from general import timer

""" Алгоритмы поиска """


@timer
def simple_search(any_list: list, item: Any) -> int | None:
    """
    Простой поиск, возвращает индекс найденного элемента или None

    Поиск перебором

    Время выполнения O(n)
    """
    for index, value in enumerate(any_list):
        if value == item:
            return index
    return None


@timer
def binary_search(sorted_list: list, item: Any) -> int | None:
    """
    Бинарный поиск, возвращает индекс елемента или None

    Берет середину списка, если больше, то отбрасывает ненужную часть, повторяет
    Если меньше, то аналогично с другой частью

    Время выполнения O(log2 n)
    """

    bottom_border = 0
    upper_border = len(sorted_list) - 1
    while bottom_border <= upper_border:
        middle = (bottom_border + upper_border) // 2
        if sorted_list[middle] == item:
            return middle
        elif sorted_list[middle] > item:
            upper_border = middle - 1
        else:
            bottom_border = middle + 1
    return None


if __name__ == '__main__':
    sorted_my_list = [i for i in range(100000000)]
    print('Простой поиск числа 21114148: (индекс):', simple_search(sorted_my_list, 21114148))
    print('Бинарный поиск числа 21114148: (индекс):', binary_search(sorted_my_list, 21114148))
