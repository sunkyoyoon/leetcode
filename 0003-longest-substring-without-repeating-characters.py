class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0 
        hashset = set()
        left = 0 
        for right in range(len(s)):
            while s[right] in hashset:
                hashset.remove(s[left])
                left += 1 
            else:
                hashset.add(s[right])
            ans = max(ans, right - left + 1)
        return ans

    # O(n) time
    # O(n) space
