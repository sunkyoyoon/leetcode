class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)
        moves = 0
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                k = r 
                while l < k and s[l] != s[k]:
                    k -= 1
                if k == l:
                    s[l], s[l+1] = s[l+1], s[l]
                    moves += 1 
                else:
                    while k < r:
                        s[k], s[k+1] = s[k+1], s[k]
                        k += 1 
                        moves += 1 
                    l += 1 
                    r -= 1 
        return moves

# O(n^2) time
# O(n) space
