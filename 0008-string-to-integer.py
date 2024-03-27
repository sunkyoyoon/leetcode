class Solution:
    def myAtoi(self, s: str) -> int:
        ans = ""
        sign = False
        start = False 
        zerostart = False
        for i in range(len(s)):
            if zerostart and s[i] == " ":
                if ans and (ans[-1] != "-" and ans[-1] != "+"):
                    if int(ans) < -2**31:
                        return -2**31
                    elif int(ans) > 2**31 - 1:
                        return 2**31 - 1
                    return int(ans)
                return 0      
            if start and not s[i].isdigit():
                if ans and (ans[-1] != "-" and ans[-1] != "+"):
                    if int(ans) < -2**31:
                        return -2**31
                    elif int(ans) > 2**31 - 1:
                        return 2**31 - 1
                    return int(ans)
                return 0     
            if sign and not s[i].isdigit():
                if ans and (ans[-1] != "-" and ans[-1] != "+"):
                    if int(ans) < -2**31:
                        return -2**31
                    elif int(ans) > 2**31 - 1:
                        return 2**31 - 1
                    return int(ans)
                return 0     
            if s[i] == " ":
                continue
            elif zerostart and (not s[i].isdigit() or s[i] == " "):
                if ans and (ans[-1] != "-" and ans[-1] != "+"):
                    if int(ans) < -2**31:
                        return -2**31
                    elif int(ans) > 2**31 - 1:
                        return 2**31 - 1
                    return int(ans)
                return 0 
            elif sign == True and (s[i] == "-" or s[i] == "+"):
                if ans and (ans[-1] != "-" and ans[-1] != "+"):
                    if int(ans) < -2**31:
                        return -2**31
                    elif int(ans) > 2**31 - 1:
                        return 2**31 - 1
                    return int(ans)
                else:
                    return 0 
            elif sign == True and not s[i].isdigit():
                if ans and (ans[-1] != "-" and ans[-1] != "+"):
                    if int(ans) < -2**31:
                        return -2**31
                    elif int(ans) > 2**31 - 1:
                        return 2**31 - 1
                    return int(ans)
                else:
                    return 0 
            elif s[i] == "-" or s[i] == "+":
                sign = True
                ans += s[i]
            elif sign and s[i].isdigit() and s[i] != "0":
                ans += s[i]
                start = True
            elif start and s[i].isdigit():
                ans += s[i]
            elif start and not s[i].isdigit():
                if ans:
                    if int(ans) < -2**31:
                        return -2**31
                    elif int(ans) > 2**31 - 1:
                        return 2**31 - 1
                    return int(ans)
                else:
                    return 0
