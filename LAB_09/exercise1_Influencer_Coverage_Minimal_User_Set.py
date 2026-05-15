from itertools import combinations


# ---------------------------------------------------------------------------
# 1. is_valid_coverage
# ---------------------------------------------------------------------------

def is_valid_coverage(selected_users: list, graph: dict) -> bool:
    """
    Check whether every node in the graph is either selected
    or directly adjacent to at least one selected node.

    Parameters
    ----------
    selected_users : list
        List of selected user/node IDs.
    graph : dict
        Adjacency list  {node_id: [neighbor_id, ...], ...}.
        Every node in the graph must appear as a key.

    Returns
    -------
    bool
        True if the selection forms a valid dominating set.

    Complexity: O(N + E)
    """
    covered = set()

    # Mark every selected node as covered
    for u in selected_users:
        covered.add(u)

    # Mark every neighbor of a selected node as covered
    for u in selected_users:
        for v in graph.get(u, []):
            covered.add(v)

    # Every node in the graph must be covered
    for node in graph:
        if node not in covered:
            return False

    return True


# ---------------------------------------------------------------------------
# 2. find_minimum_coverage
# ---------------------------------------------------------------------------

def find_minimum_coverage(graph: dict) -> tuple:
    """
    Find the exact minimum dominating set by iterating over subsets
    in increasing size order and returning as soon as the first valid
    (and therefore smallest) dominating set is found.

    Parameters
    ----------
    graph : dict
        Adjacency list {node_id: [neighbor_id, ...], ...}.

    Returns
    -------
    (int, list)
        (size_of_minimum_set, list_of_selected_users)

    Complexity: O(2^N * (N + E))  — correct for N ≤ 20
    """
    nodes = list(graph.keys())
    n = len(nodes)

    size = n + 1                    
    list_of_selected_users = []

    for selected_num in range(1, n + 1):
        all_candidates = combinations(nodes, selected_num)

        for selected_users in all_candidates:
            if len(selected_users) >= size:
                continue

            if is_valid_coverage(list(selected_users), graph):
                size = len(selected_users)
                list_of_selected_users = list(selected_users)
                return (size, list_of_selected_users)

    return (size, list_of_selected_users)


# ---------------------------------------------------------------------------
# Helper for find_fast_coverage
# ---------------------------------------------------------------------------

def _count_covered(u, uncovered: set, graph: dict) -> int:
    """
    Count how many currently uncovered nodes would be dominated
    by selecting node u  (u itself + its uncovered neighbours).

    Complexity: O(deg(u))
    """
    count = 1 if u in uncovered else 0
    for v in graph.get(u, []):
        if v in uncovered:
            count += 1
    return count


# ---------------------------------------------------------------------------
# 3. find_fast_coverage
# ---------------------------------------------------------------------------

def find_fast_coverage(graph: dict) -> tuple:
    """
    Greedy approximation for the minimum dominating set.

    At each step, select the node that covers the most currently
    uncovered nodes (itself + uncovered neighbours), until every
    node is dominated.

    Parameters
    ----------
    graph : dict
        Adjacency list {node_id: [neighbor_id, ...], ...}.

    Returns
    -------
    (int, list)
        (size_of_selected_set, list_of_selected_users)

    Complexity: O(N * (N + E))
    """
    uncovered_nodes = set(graph.keys())
    list_of_selected_users = []

    while uncovered_nodes:
        best_node = None
        max_coverage = -1

        for u in graph:
            current_gain = _count_covered(u, uncovered_nodes, graph)
            if current_gain > max_coverage:
                max_coverage = current_gain
                best_node = u

        list_of_selected_users.append(best_node)

        uncovered_nodes.discard(best_node)
        for neighbor in graph.get(best_node, []):
            uncovered_nodes.discard(neighbor)

    size = len(list_of_selected_users)
    return (size, list_of_selected_users)