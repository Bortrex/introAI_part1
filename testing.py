from queue import PriorityQueue
import numpy as np
def dfs(graph, start, goal):
    visited = []
    path = []
    fringe = PriorityQueue()
    fringe.put((0, start, path, visited))

    while not fringe.empty():
        depth, current_node, path, visited = fringe.get()
        print(current_node, type(current_node))

        if current_node == goal:
            return path + [current_node]

        visited = visited + [current_node]

        child_nodes = graph[current_node]
        # print(child_nodes)
        for node in child_nodes:
            if node not in visited:
                if node == goal:
                    return path + [node]
                depth_of_node = len(path)
                fringe.put((-depth_of_node, node, path + [node], visited))

    return path
# def dfs(graph, start, goal):
#     stack = [(start, [start])]
#     while stack:
#         (vertex, path) = stack.pop()
#         for next in graph[vertex] - set(path):
#             print(graph[vertex])
#             print(path)
#             # print(type(graph[vertex]), type(set(path)))
#             # print(next)
#             print(graph[vertex] - set(path), "\n")
#         # for next in graph[vertex] - np.array(path):
#             if next == goal:
#                 yield path + [next]
#             else:
#                 stack.append((next, path + [next]))


if __name__ == "__main__":
    graph = {
        (1,1): set([(1,2), (2,1)]),
        (1,2): set([ (1,3), (1,1),  (2,2)]),
        (1,3): set([(1,4), (1,2)]),
        (1,4): set([(1,3), (2,4)]),
        (2,1): set([(1,1), (3,1)]),
        (2,2): set([(2,3), (1,2)]),
        (2,3): set([(2,2)]),
        (2,4): set([(1,4), (3,4)]),
        (3,1): set([(2,1), (3,2)]),
        (3,2): set([(3,1), (3,3)]),
        (3,3): set([(3,2), (3,4)]),
        (3,4): set([(2,4), (3,3)]),

    #     (1, 1): ([(1, 2), (2, 1)]),
    #     (1, 2): ([(1, 3), (1, 1), (2, 2)]),
    #     (1, 3): ([(1, 4), (1, 2)]),
    #     (1, 4): ([(1, 3), (2, 4)]),
    #     (2, 1): ([(1, 1), (3, 1)]),
    #     (2, 2): ([(2, 3), (1, 2)]),
    #     (2, 3): ([(2, 2)]),
    #     (2, 4): ([(1, 4), (3, 4)]),
    #     (3, 1): ([(2, 1), (3, 2)]),
    #     (3, 2): ([(3, 1), (3, 3)]),
    #     (3, 3): ([(3, 2), (3, 4)]),
    #     (3, 4): ([(2, 4), (3, 3)]),
    }
    # print(list(graph.items())[1])
    # path = dfs(graph, (2,4), (2,3))


    path = list(dfs(graph, (1,2), (2,3)))
    print("path", path) # ==> [(1,2), (2,2), (2,3)]