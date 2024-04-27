class Solution:
    def isValid(self, s: str) -> bool:
        op = {"(":")", "[":"]", "{":"}"}
        cl = {")":"(","]":"[","}":"{"}
        stack = [] 
        for b in s:
            if b in op:
                stack.append(b)
            elif b in cl:
                if stack and stack[-1] == cl[b]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        
        return stack == [] 
