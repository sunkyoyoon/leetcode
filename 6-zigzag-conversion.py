class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = ""
        table = [["" for _ in range(len(s))] for _ in range(numRows)]
        
        other = False  
        row = numRows - 2 
        col = 0 
        index = 0 
        while index <= len(s) - 1:
            if numRows - 1 > 0 and col % (numRows - 1) == 0: 
                for i in range(numRows):
                    if index <= len(s) - 1:
                        table[i][col] = s[index]
                        index += 1
            else:
                if index <= len(s) - 1:
                    table[row][col] = s[index]
                    row -= 1 
                    index += 1
                if row < 1:
                    row = numRows - 2
            
            col += 1 

        row = 0 
        index = 0 
        while len(ans) != len(s):
            for k in range(len(s)):
                if table[row][k]:
                    ans += table[row][k]
            row += 1 
        
        return ans
