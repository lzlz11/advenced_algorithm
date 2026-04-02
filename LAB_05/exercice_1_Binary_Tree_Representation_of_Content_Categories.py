
class CategoryNode:
    def __init__(self, category_id: int, name: str, post_count: int):
        self.category_id = category_id  
        self.name = name              
        self.post_count = post_count    
        self.left = None               
        self.right = None               
        self.parent = None              

# Height of trees
def calculate_height(node):
    if node == None:
        return -1
    left_h = calculate_height(node.left)
    right_h = calculate_height(node.right)
    return max(left_h, right_h) + 1

# Find the target node
def find_category(target_id, node):
    if node is None:
        return None
    if node.category_id == target_id:
        return node
    left_result = find_category(target_id, node.left)
    if left_result:
        return left_result
    return find_category(target_id, node.right)

# node height
def calculate_node_height(node, target_id):
    target_node = find_category(target_id, node)
    if target_node == None:
        return -1
    return calculate_height(target_node)

# find the total number of nodes
def count_nodes(node):
    if node == None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

# find the total number of leaves
def count_leaves(node):
    if node == None:
        return 0
    if node.left == None and node.right == None:
        return 1
    return count_leaves(node.right) + count_leaves(node.left)

# tress balance
def is_balanced(node):
    if node == None:
        return True
    left_h = calculate_height(node.left)
    right_h = calculate_height(node.right)
    if abs(left_h - right_h) > 1:
        return False
    return is_balanced(node.left) and is_balanced(node.right)

# Determine if a binary tree is full
def is_full_binary_tree(node):
    if node == None:
        return True
    if node.left == None and node.right == None:
        return True
    if node.left != None and node.right != None:
        return is_full_binary_tree(node.left) and is_full_binary_tree(node.right)
    return False

# Determine a perfect tree
def is_perfect_binary_tree(node):
    height = calculate_height(node)
    node_count = count_nodes(node)
    perfect_count = 2 ** (height + 1) - 1
    return node_count == perfect_count

# Auxiliary function
def is_complete_helper(node, index, total_nodes):
    if node == None:
        return False
    if index > total_nodes:
        return False
    return is_complete_helper(node.left, index * 2, total_nodes) and is_complete_helper(node.right, index * 2 + 1, total_nodes)

# Determine if a binary tree is complete
def is_complete_binary_tree(node):
    total = count_nodes(node)
    return is_complete_helper(node, 1, total)

# Find category nodes by ID
def find_category(target_id, node):
    if node == None:
        return None
    if node.category_id == target_id:
        return node
    left_result = find_category(target_id, node.left)
    if left_result != None:
        return left_result
    return find_category(target_id, node.right)

# Find the path from the target node to the root node.
def find_path_to_root(target_id, node):
    path = []
    target_node = find_category(target_id, node)
    if target_node == None:
        return path
    current = target_node
    while current != None:
        path.append(current.name)
        current = current.parent
    return path

# Find the lowest common ancestor of two nodes.
def lowest_common_ancestor(id1, id2, node):
    path1 = find_path_to_root(id1, node)
    path2 = find_path_to_root(id2, node)
    if len(path1) == 0 or len(path2) == 0:
        return None
    i = len(path1) - 1
    j = len(path2) - 1
    lca = None
    while i >= 0 and j >= 0 and path1[i] == path2[j]:
        lca = path1[i]
        i = i - 1
        j = j - 1
    if lca != None:
        return find_category(lca, node)
    return None