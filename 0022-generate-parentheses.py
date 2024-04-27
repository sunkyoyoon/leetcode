class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = [] 
        def backtrack(op, cl, curr):
            if len(curr) == n*2 and op != cl:
                return 
            if len(curr) == n*2 and op == cl:
                ans.append(curr)
                return
            if op > cl:
                curr += ")"
                backtrack(op,cl+1,curr)
                curr = curr[0:len(curr)-1]
                
                curr += "("
                backtrack(op+1,cl,curr)
                curr = curr[0:len(curr)-1]
            elif op == cl:
                curr += "("
                backtrack(op+1,cl,curr)
                curr = curr[0:len(curr)-1]

        backtrack(0,0,"")
        return ans

'''
(()),()()

((())), (()())
'''
