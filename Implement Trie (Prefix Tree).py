class Trie:

    def __init__(self):
        self.t = defaultdict(lambda: None)
        self.t["word"] = False

    def insert(self, word: str) -> None:
        itr = self.t
        for c in word[:-1]:
            if not itr[c]:
                itr[c] = defaultdict(lambda: None)
                itr[c]["word"] = False
            itr = itr[c]
        c = word[-1]
        if not itr[c]:
            itr[c] = defaultdict(lambda: None)
        itr[c]["word"] = True

    def search(self, word: str) -> bool:
        itr = self.t
        for c in word[:-1]:
            if not itr[c]:
                return False
            itr = itr[c]
        c = word[-1]
        if itr[c]:
            return itr[c]["word"]
        return False

    def startsWith(self, prefix: str) -> bool:
        itr = self.t
        for c in prefix:
            if not itr[c]:
                return False
            itr = itr[c]  
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)