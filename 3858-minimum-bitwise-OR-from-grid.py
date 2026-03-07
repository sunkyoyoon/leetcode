class Solution:
    def minimumOR(self, grid: List[List[int]]) -> int:
        ans = (1 << 31) - 1 
        for i in range(30,-1,-1):
            candidate = ans ^ (1 << i)
            for row in grid:
                ok = False 
                for r in row:
                    if candidate | r == candidate:
                        ok = True
                        break 
                if ok == False:
                    break
            if ok == True:
                ans = candidate

        return ans 
                


