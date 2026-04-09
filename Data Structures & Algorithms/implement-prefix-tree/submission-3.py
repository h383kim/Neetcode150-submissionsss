class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char in cur.children:
                cur = cur.children[char]
            else:
                cur.children[char] = Node()
                cur = cur.children[char]
        cur.flag = True

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char in cur.children:
                cur = cur.children[char]
            else:
                return False
        return cur.flag

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if char in cur.children:
                cur = cur.children[char]
            else:
                return False
        return True

class Node():
    def __init__(self):
        self.children = {}
        self.flag = False