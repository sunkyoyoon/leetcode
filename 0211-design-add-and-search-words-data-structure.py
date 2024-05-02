class TrieNode():
    def __init__(self):
        self.children = {} 
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True
        
    def search(self, word: str) -> bool:
        curr = self.root
        return self.helper(curr, word)

    def helper(self, curr, word):
        if not word:
            return curr.end
        for i in range(len(word)):
            c = word[i]
            if c != ".":
                if c not in curr.children:
                    return False 
                else:
                    curr = curr.children[c]
            if c == ".":
                for child in curr.children:
                    if self.helper(curr.children[child], word[i+1:]):
                        return True
                return False
            
        return curr.end


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
