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
