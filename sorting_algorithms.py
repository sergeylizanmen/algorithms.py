import random
from general import timer

""" Алгоритмы сортировки """


@timer
def selection_sort(unsorted_list: list) -> list:
    """
    Сортировка выбором в порядке возрастания

    Находит элементы по возрастанию и сразу ставит их на место в списке

    Время выполнения O(n^2)
    """

    for index, value in enumerate(unsorted_list):
        min_index = min(
            range(index, len(unsorted_list)),
            key=lambda item_index: unsorted_list[item_index]
        )

        unsorted_list[index], unsorted_list[min_index] = unsorted_list[min_index], value

    return unsorted_list


def quick_sort(unsorted_list: list) -> list:
    """
    Быстрая сортировка

    По опорному определяет все меньшие, большие и равные элементы
    повторяет Рекурсией пока не останутся списки из 0 или 1 элемента
    соединяет все списки в порядке стека


    Время выполнения O(n * log2 n)
    """
    if len(unsorted_list) <= 1:
        return unsorted_list

    pivot = unsorted_list[len(unsorted_list) // 2]
    smaller_elements = [i for i in unsorted_list if i < pivot]
    bigger_elements = [i for i in unsorted_list if i > pivot]
    equal_pivot = [i for i in unsorted_list if i == pivot]
    return quick_sort(smaller_elements) + equal_pivot + quick_sort(bigger_elements)


@timer
def bubble_sort(unsorted_list: list) -> list:
    """
    Пузырьковая сортировка

    Попарно меняем местами элементы, после каждого перебора
    на нужное место встает наибольший элемент

    Время выполнения O(n^2)
    """
    n = 1
    while len(unsorted_list) - n > 1:
        for index in range(len(unsorted_list) - n):
            if unsorted_list[index] > unsorted_list[index + 1]:
                unsorted_list[index], unsorted_list[index + 1] = unsorted_list[index + 1], unsorted_list[index]
        n += 1
    return unsorted_list


if __name__ == '__main__':
    my_list = [random.randint(0, 10) for i in range(10)]
    print('Изначальный список:', my_list)
    print('Быстрая сортировка:', timer(quick_sort)(my_list[:]))
    print('Сортировка выбором:', selection_sort(my_list[:]))
    print('Сортировка пузырьком:', bubble_sort(my_list[:]))
