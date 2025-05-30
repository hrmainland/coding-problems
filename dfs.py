from dataclasses import dataclass

values = [4, 6, 2, 3, 45]
adj = [[0, 1], [0, 2], [1, 2], [1, 4], [2, 3]]


def create_adj_list(values, adj):
    result = [[] for elem in values]
    for v1, v2 in adj:
        result[v1].append(v2)
    return result


def dfs(node: int, values: list, adj_list: list, path: list, path_set: set):
    path.append(node)
    path_set.add(node)
    max_path = []
    for child in adj_list[node]:
        if child not in path_set:
            dfs_result = dfs(child, values, adj_list, path, path_set)
            if len(dfs_result) > len(max_path):
                max_path = dfs_result
    if not max_path:
        max_path = path[::]
    path.pop(len(path) - 1)
    path_set.remove(node)
    return max_path


@dataclass
class PathObj:
    node: int
    path: list


def stack_dfs(start_node, adj_list):
    max_path = []
    stack = [PathObj(start_node, [start_node])]
    while stack:
        path_obj = stack.pop(0)
        node = path_obj.node
        path = path_obj.path
        if len(path) > len(max_path):
            max_path = path
        children = adj_list[node]
        for child in children:
            if child not in path:
                stack.insert(0, PathObj(child, path + [child]))
    return max_path


# def dfs(node, values, adj_list, visited, path):
#     path.append(node)
#     visited.add(node)
#     max_path = []
#     for child in adj_list[node]:
#         if child not in visited:
#             dfs_result = dfs(child, values, adj_list, visited, path)
#             if len(dfs_result) > len(max_path):
#                 max_path = dfs_result
#     if not max_path:
#         max_path = path[::]
#     path.pop(len(path) - 1)
#     return max_path


def stack_dfs_path(start_node, adj_list):
    max_path = []

    # Each item is (current_node, path_so_far, value_sum_so_far)
    stack = [(start_node, [start_node])]
    while stack:
        node, path = stack.pop()
        if len(path) > len(max_path):
            max_path = path
        for child in adj_list[node]:
            if child not in path:  # avoid cycles
                stack.append((child, path + [child]))

    return max_path


adj_list = create_adj_list(values, adj)
visited = set()
path = []
# print(dfs(0, values, adj_list, path, set()))
print(stack_dfs_path(0, adj_list))
