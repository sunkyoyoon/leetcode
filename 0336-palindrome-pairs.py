class TrieNode:
    def __init__(self):
        self.next = defaultdict(TrieNode)
        self.end = -1 
        self.palindrome_suffix = [] 

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = TrieNode()
        for i, word in enumerate(words):
            word = word[::-1]
            curr = trie
            for j, c in enumerate(word):
                if word[j:] == word[j:][::-1]:
                    curr.palindrome_suffix.append(i)
                curr = curr.next[c]
            curr.end = i

        solutions = [] 
        for i, word in enumerate(words):
            curr = trie
            for j, c in enumerate(word):
                if curr.end != -1:
                    if word[j:] == word[j:][::-1]:
                        solutions.append([i, curr.end])
                if c not in curr.next:
                    break
                curr = curr.next[c]
            
            else:
                if curr.end != -1 and curr.end != i:
                    solutions.append([i,curr.end])
                for j in curr.palindrome_suffix:
                    solutions.append([i,j])
        return solutions
