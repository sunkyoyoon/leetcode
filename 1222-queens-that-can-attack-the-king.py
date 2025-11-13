class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:

        ans = []
        kr, kc = king
        for r in range(kr,8):
            if [r, kc] in queens:
                ans.append([r, kc])
                break

        for r in range(8):
            if [kr - r, kc] in queens:
                ans.append([kr - r, kc])
                break

        for c in range(kc,8):
            if [kr, c] in queens:
                ans.append([kr,c])
                break
        for c in range(8):
            if [kr, kc - c] in queens:
                ans.append([kr, kc - c])
                break

        for i in range(8):
            if [kr - i, kc - i] in queens:
                ans.append([kr - i, kc - i])
                break
        for i in range(8):
            if [kr + i, kc - i] in queens:
                ans.append([kr + i, kc - i])
                break
        for i in range(8):
            if [kr - i, kc + i] in queens:
                ans.append([kr - i, kc + i])
                break
        for i in range(8):
            if [kr + i, kc + i] in queens:
                ans.append([kr + i, kc + i])
                break

        return ans


                    
                    


