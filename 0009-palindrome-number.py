class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x[0] == "-" or x[0] == "+":
            return False 
        mid = len(x) // 2 

        left = mid if len(x) % 2 else mid - 1 
        right = mid if len(x) % 2 else mid 

        while left >= 0 and right <= len(x) - 1 and x[left] == x[right]:
            left -= 1 
            right += 1
        
        if left < 0 and right > len(x) - 1:
            return True 
        else:
            return False


