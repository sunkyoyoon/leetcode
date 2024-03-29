class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        if num % 10:
            x = num % 10
            if x == 4:
                ans += "VI"
            elif x == 9:
                ans += "XI"
            else:
                if x >= 5:
                    for _ in range(x-5):
                        ans += "I"
                    ans += "V"
                else: 
                    for _ in range(x):
                        ans += "I"

        num //= 10 
        if num % 10:
            x = num % 10 
            if x == 4:
                ans += "LX"
            elif x == 9:
                ans += "CX"
            else:
                if x >= 5:
                    for _ in range(x-5):
                        ans += "X"
                    ans += "L"
                else: 
                    for _ in range(x):
                        ans += "X"

        num //= 10 
        if num % 10:
            x = num % 10 
            if x == 4:
                ans += "DC"
            elif x == 9:
                ans += "MC"
            else:
                if x >= 5:
                    for _ in range(x-5):
                        ans += "C"
                    ans += "D"
                else: 
                    for _ in range(x):
                        ans += "C"
        num //= 10
        if num % 10:
            x = num % 10 
            for _ in range(x):
                ans += "M"
        
        return ans[::-1]
