class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        skip = False 
        for i in range(len(s)):
            if skip:
                skip = False
                continue
            if (i+1) <= len(s) - 1 and s[i] == "I" and s[i+1] == "V":
                ans += 4
                skip = True
            elif (i+1) <= len(s) - 1 and s[i] == "I" and s[i+1] == "X":
                ans += 9
                skip = True
            elif (i+1) <= len(s) - 1 and s[i] == "X" and s[i+1] == "L":
                ans += 40
                skip = True
            elif (i+1) <= len(s) - 1 and s[i] == "X" and s[i+1] == "C":
                ans += 90
                skip = True
            elif (i+1) <= len(s) - 1 and s[i] == "C" and s[i+1] == "D":
                ans += 400
                skip = True
            elif (i+1) <= len(s) - 1 and s[i] == "C" and s[i+1] == "M":
                ans += 900
                skip = True
            else:
                if s[i] == "M":
                    ans += 1000 
                elif s[i] == "D":
                    ans += 500 
                elif s[i] == "C":
                    ans += 100 
                elif s[i] == "L":
                    ans += 50
                elif s[i] == "X":
                    ans += 10
                elif s[i] == "V":
                    ans += 5 
                elif s[i] == "I":
                    ans += 1 
        return ans
