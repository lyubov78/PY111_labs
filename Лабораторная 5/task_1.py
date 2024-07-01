from typing import Union

import networkx as nx


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    ...  # TODO c помощью функции из модуля networkx найти стоимость кратчайшего пути до последней лестницы
    return nx.dijkstra_path_length(graph, 0, len(graph.nodes) - 1)


if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    stairway_graph = nx.DiGraph()  # TODO записать взвешенный граф, а лучше написать функцию, которая формирует граф по стоимости ступеней

    for i in range(len(stairway)):
        stairway_graph.add_edge(i, i + 1, weight=stairway[i])
        if i + 2 <= len(stairway):
            stairway_graph.add_edge(i, i + 2, weight=stairway[i + 1])

    print(stairway_path(stairway_graph))  # 72
