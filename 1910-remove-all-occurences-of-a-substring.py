class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = [] 
        for i in range(len(s)):
            stack.append(s[i])
            if len(stack) >= len(part):
                found = True 
                for j in range(len(part)):
                    if stack[-j-1] != part[-j-1]:
                        found = False
                        break
                if found:
                    for k in range(len(part)):
                        stack.pop()
        return "".join(stack)
                        
