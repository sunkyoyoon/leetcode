class Solution:
    def decodeString(self, s: str) -> str:
        ans = ""
        stack = [] 
        for i in range(len(s)):
            c = s[i]
            if c != ']':
                stack.append(c)
            
            if c == ']':
                temp = ""
                while stack and stack[-1] not in "0123456789":
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        tmp = stack.pop()[::-1]
                        temp += tmp
                
                temp = temp[::-1]
                
                num = ""
                while stack and stack[-1] in "0123456789":
                    num += stack.pop()
                num = num[::-1]
                

                if num != "":
                    for _ in range(int(num)):
                        stack.append(temp)

        return "".join(stack)


