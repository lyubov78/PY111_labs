"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        TODO Описать где начало и конец очереди
        Начало очереди: индекс 0
        Конец очереди: индекс -1
        """
        ...  # TODO инициализировать список
        self._queue = []

    def enqueue(self, elem: Any) -> None:   # O(1)
        """
        Добавление элемент в конец очереди

        :param elem: Элемент, который должен быть добавлен
        """
        ...  # TODO реализовать метод enqueue
        self._queue.append(elem)

    def dequeue(self) -> Any:    # O(1)
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        ...  # TODO реализовать метод dequeue
        if not self._queue:
            raise IndexError("Очередь пуста")
        return self._queue.pop(0)

    def peek(self, ind: int = 0) -> Any:     # O(1)
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        ...  # TODO реализовать метод peek
        if not isinstance(ind, int):
            raise TypeError(f"Ошибка! Индекс должен быть типа int, а не {type(ind).__name__}")

        if not 0 <= ind <= len(self._queue):
            raise IndexError(f"Ошибка! Индекс должен быть от 0 до {len(self._queue) - 1}")

        return self._queue[ind]

    def clear(self) -> None:     # O(1)
        """ Очистка очереди. """
        ...  # TODO реализовать метод clear
        self._queue.clear()

    def __len__(self):   # O(1)
        """ Количество элементов в очереди. """
        ...  # TODO реализовать метод __len__
        return len(self._queue)
