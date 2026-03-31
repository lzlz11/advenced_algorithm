import random
class CategoryNode:
    def __init__(self, name,post_count, parent):
        self.category_id = random.randint(1, 100000)
        self.name = name
        self.post_count = post_count
        self.left = None
        self.right = None
        self.parent = parent
        if parent:
            if parent.left:
                if parent.right:
                    print("invalid parent, node already have two child")
                else:
                    parent.right = self
            else:
                parent.left = self

    def add_child_left(self, node):
        self.left = node
    def add_child_right(self, node):
        self.right = node



    def __str__(self):
        return f"{self.name}, count: {self.post_count}, left: {self.left}, right: {self.right}"

def in_order(node,original_node = None, solution = []):
    if original_node is None:
        original_node = node
    if node == original_node and node.right in solution:
        return solution
    if node.left is None or node.left in solution:
        if node.right is None:
            solution.append(node)
            return in_order(node.parent, original_node, solution)
        elif node.right in solution:
            return in_order(node.parent, original_node, solution)
        else:
            solution.append(node)
            return in_order(node.right, original_node, solution)
    else:
        return in_order(node.left, original_node, solution)



def in_order_collect(node):
    array = in_order(node)
    result = []
    if array:
        for node in array:
            result.append(node.name + f"({node.post_count})")
    return result

def in_order_accumulate_posts(node):
    array = in_order(node)
    total = 0
    for node in array:
        total += node.post_count
    return total

def in_order_find_kth(k, node):
    array = in_order(node)
    if len(array) < k:
        return None
    else:
        return array[k-1]

Technology = CategoryNode("Technology", 150, None)
Programing = CategoryNode("Programing", 85, Technology)
Python = CategoryNode("Python", 42, Programing)
Django = CategoryNode("Django", 18, Python)
Flask = CategoryNode("Flask", 12, Python)
Java = CategoryNode("Java", 13, Programing)
Design = CategoryNode("Design", 14, Technology)
UI = CategoryNode("UI", 15, Design)
Graphics = CategoryNode("Graphics", 16, Design)


print(in_order_collect(Technology))
print(in_order_collect(Design))
print(in_order_accumulate_posts(Design))
print(in_order_find_kth(5,Programing))