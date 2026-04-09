class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char in cur.children:
                cur = cur.children[char]
            else:
                cur.children[char] = Node()
                cur = cur.children[char]
        cur.flag = True
    

    def search(self, word: str) -> bool:
        return self.search_from(word, self.root)

    def search_from(self, word, start):
        cur = start
        for idx, char in enumerate(word):
            if char == ".":
                for branch in cur.children.values():
                    if self.search_from(word[idx + 1:], branch):
                        return True
                return False
            else:
                if char in cur.children:
                    cur = cur.children[char]
                else:
                    return False
        return cur.flag   

class Node():
    def __init__(self):
        self.children = {}
        self.flag = False