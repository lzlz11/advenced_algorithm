def is_valid_invitation(invited, graph):
    for i in range(len(invited)):
        for j in range(len(invited) - 1, -1, -1):
            u = invited[i]
            v = invited[j]
            if v in graph[u]:
                return False
    return True


def find_max_invitations_exact(graph):
    n = graph.num_nodes()
    Nodes = graph.all_nodes()
    best_size = 0
    best_set = []
    
    def backtrack(candidates, current_set):
        nonlocal best_size, best_set
        
        if len(current_set) + len(candidates) <= best_size:
            return
        
        # if no candidate nodes
        if not candidates:
            if len(current_set) > best_size:
                best_size = len(current_set)
                best_set = current_set.copy()
            return
        
        v = candidates[0]
        rest = candidates[1:]
        
        # branch1: choose node v
        new_candidates = []
        for u in rest:
            if u not in graph[v]:
                new_candidates.append(u)
        
        backtrack(new_candidates, current_set + [v])
        
        # branch2: not choose node v
        backtrack(rest, current_set)
    
    backtrack(Nodes, [])
    return (best_size, best_set)


def find_max_invitations_greedy(graph):

    def count_remove(u, remaining_graph):
        """
        Calculate the number of nodes (u and all its neighbors)
          that need to be removed when selecting node u.
        """
        count = 1
        for v in remaining_graph.neighbors(u):
            count += 1
        return count
    
    # copy of graph
    import copy
    remaining_graph = copy.deepcopy(graph)
    list_of_selected_users = []
    
    while True:
        if not remaining_graph.all_nodes():
            break
        
        best_node = None
        min_removal = float('inf')
        
        # Find the node with the fewest neighbors to remove.
        for u in remaining_graph.all_nodes():
            current_removal = count_remove(u, remaining_graph)
            if current_removal < min_removal:
                min_removal = current_removal
                best_node = u
        
        list_of_selected_users.append(best_node)
        
        # Remove the best node and all its neighbors.
        to_remove = [best_node] + remaining_graph.neighbors(best_node)
        
        for w in to_remove:
            remaining_graph.remove_node(w)
            for x in remaining_graph.all_nodes():
                remaining_graph.remove_edge(x, w)
    
    size = len(list_of_selected_users)
    return (size, list_of_selected_users)