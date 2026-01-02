class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        l, r = p.split("*")

        if l:
            l_found = False
        else:
            l_found = True 
        if r:
            r_found = False 
        else:
            r_found = True 

        for i in range(len(s)):
            j = 0 
            if l_found == False:
                while j < len(l) and i < len(s) and s[i] == l[j]:
                    i += 1 
                    j += 1 
                if i == len(s) and r_found == False:
                    return False 
                if j == len(l):
                    l_found = True
                    if r_found == True:
                        return True 
            
            if l_found == True and r_found == False:
                for k in range(i, len(s)):
                    j = 0 
                    while j < len(r) and k < len(s) and s[k] == r[j]:
                        k += 1 
                        j += 1 
                    if j == len(r):
                        return True 
                return False

            elif l_found == True and r_found == True:
                return True 
        return False

