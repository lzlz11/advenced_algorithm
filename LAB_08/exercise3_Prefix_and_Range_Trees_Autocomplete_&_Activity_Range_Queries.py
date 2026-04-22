from exo3_usernames import usernames
import random

class user:
    def __init__(self, name):
        self.name = name
        self.user_id = random.randint(1, 10000)

class trie_node:
    def __init__(self, letter, parent):
        self.children = []
        self.letter = letter
        self.is_end_username = False
        self.user_id = 0
        self.parent = parent

    def add_child(self, letter, parent=None):
        self.children.append(trie_node(letter,parent))

    def end_username(self):
        self.is_end_username = True

class trie:
    def __init__(self):
        self.root = trie_node('',None)

    def search_trie(self, user_name, letter = None):
        if letter is None:
            letter = self.root
        if user_name == '':
            if not letter.is_end_username:
                return None
            else:
                return letter.user_id
        if not letter.children:
            return None
        for i in letter.children:
            if i.letter == user_name[0]:
                return self.search_trie(user_name[1:], i)
        return None

    def insert(self, user):
        path = ""
        curr_letter = self.root
        for letters in user.name:
            if not curr_letter.children == []:
                letter_found = False
                for n in curr_letter.children:
                    if n.letter == letters:
                        letter_found = True
                        curr_letter = n
                        break
                if not letter_found:
                    curr_letter.children.append(trie_node(letters, curr_letter))
                    curr_letter = curr_letter.children[-1]
            else:
                curr_letter.children.append(trie_node(letters, curr_letter))
                curr_letter = curr_letter.children[0]
        curr_letter.user_id = user.user_id
        curr_letter.is_end_username = True

    def start_with(self, prefix, node = None):
        if node is None:
            node = self.root
        if prefix == '':
            if not node.children:
                return False
            else:
                return True
        if not node.children:
            return False
        return self.start_with(prefix[1:], node)

    def autocomplete(self, prefix, max_result = 10):
        result = []
        node = self.root
        for letters in prefix:
            letter_found = False
            for n in node.children:
                if n.letter == letters:
                    node = n
                    letter_found = True
                    break
            if not letter_found:
                return result
        nodes_to_visit = [(node, "")]
        while nodes_to_visit and len(result) < max_result:
            node, string = nodes_to_visit.pop(0)
            for n in node.children:
                nodes_to_visit.append((n, string + node.letter))
            if node.is_end_username:
                result.append(string[1:] + node.letter)
        return result

    def count_words(self):
        count = 0
        nodes = [self.root]
        while nodes:
            node = nodes.pop(0)
            for n in node.children:
                nodes.append(n)
            if node.is_end_username:
                count += 1
        return count

    def get_height(self):
        max_length = 0
        nodes = [(self.root,0)]
        while nodes:
            node,height = nodes.pop(0)
            for n in node.children:
                nodes.append((n,height + 1))
            if height > max_length:
                max_length = height
        return max_length

    def get_total_nodes(self):
        count = -1
        nodes = [self.root]
        while nodes:
            node = nodes.pop(0)
            count += 1
            for n in node.children:
                nodes.append(n)
        return count

    def delete(self, username):
        if not self.search_trie(username):
            return "user not found"
        node = self.root
        for letter in username:
            for n in node.children:
                if n.letter == letter:
                    node = n
                    break
        node.is_end_username = False
        while not node.children:
            node_parent = node.parent
            node.parent = None
            for i in range(len(node_parent.children)):
                if node == node_parent.children[i]:
                    node_parent.children.pop(i)
                    break
            node = node_parent
        return "user deleted"

    def print_trie(self):
        def _print_node(node, prefix="", is_last=True, is_root=True):
            if is_root:
                print("(root)")
            else:
                connector = "└── " if is_last else "├── "
                label = f"{node.letter}"
                if node.is_end_username:
                    label += "  ●"
                print(prefix + connector + label)

            child_prefix = prefix + ("    " if is_last else "│   ")
            for i, child in enumerate(node.children):
                _print_node(child, child_prefix, i == len(node.children) - 1, False)

        _print_node(self.root)



print("\n---------- Part A: Trie for autocomplete ----------\n")
user1 = user("user1")
user2 = user("user2")
user3 = user("user3")
michel = user("michel")
mark = user("mark")
marguerite = user("marguerite")
ursula = user("ursula")
ursul = user("ursul")



trie = trie()
trie.insert(user1)
trie.insert(user2)
trie.insert(user3)
trie.insert(michel)
trie.insert(mark)
trie.insert(marguerite)
trie.insert(ursula)
trie.insert(ursul)

print("the trie:")
trie.print_trie()

print("trie search for mark: ", trie.search_trie("mark"))

print("start with function with ma: ", trie.start_with("ma"))
print("autocomplete function with ma: ", trie.autocomplete("ma"))
print("count words function: ", trie.count_words())
print("get height function: ", trie.get_height())
print("get total nodes function: ", trie.get_total_nodes())
trie.delete("michel")
print("Trie after michel deletion:")
trie.print_trie()

print("insertion of 50000 usernames")
for username in usernames:
    trie.insert(user(username))


print("autocomplete function with ammar: ", trie.autocomplete("ammar"))
print("count words function: ", trie.count_words())
print("get height function: ", trie.get_height())
print("get total nodes function: ", trie.get_total_nodes())
