
import random

class user:
    def __init__(self, name):
        self.name = name
        self.user_id = random.randint(1, 10000)

class trie_node:
    def __init__(self, letter):
        self.children = []
        self.letter = letter
        self.is_end_username = False
        self.user_id = 0

    def add_child(self, letter, node):
        self.children.append(trie_node(letter))

    def end_username(self):
        self.is_end_username = True

class trie:
    def __init__(self):
        self.root = trie_node('')

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
            if i == user_name[0]:
                return self.search_trie(i, user_name[1:])
        return None

    def insert(self, user):
        path = ""
        curr_letter = self.root
        for letters in user.name:
            if not curr_letter.children == []:
                for n in curr_letter.children:
                    if n.letter == letters:
                        curr_letter = n
                        path += n.letter
                        break
            else:
                path += curr_letter.letter
                curr_letter.children.append(trie_node(letters))
                curr_letter = curr_letter.children[0]
        curr_letter.user_id = user.user_id
        curr_letter.is_end_username = True
        print(path)

print("1"[1:] == "")
user1 = user("user1")
user2 = user("user2")
user3 = user("user3")



trie = trie()
trie.insert(user1)
trie.insert(user2)