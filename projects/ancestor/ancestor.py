
def earliest_ancestor(ancestors, starting_node):
    # make a graph: k = child, v = [parent(s)]
    ancestor_graph = {}
    for pair in ancestors:
        if pair[1] not in ancestor_graph:
            ancestor_graph[pair[1]] = [pair[0]]
        else:
            ancestor_graph[pair[1]].append(pair[0])

    # in case we start on a parent:
    if starting_node not in ancestor_graph:
        return -1

    # DFS for longest ancestry
    longest_ancestry = [starting_node]
    s = [longest_ancestry]
    while len(s) > 0:
        ancestry = s.pop()
        child = ancestry[-1]
        if child in ancestor_graph:
            for parent in ancestor_graph[child]:
                new_ancestry = ancestry[:]  # fresh copy
                new_ancestry.append(parent)
                s.append(new_ancestry)
        else:
            # no parents, potential oldest ancestor
            if len(ancestry) > len(longest_ancestry):
                longest_ancestry = ancestry
            elif len(ancestry) == len(longest_ancestry):
                if ancestry[-1] < longest_ancestry[-1]:
                    longest_ancestry = ancestry
    return longest_ancestry[-1]
