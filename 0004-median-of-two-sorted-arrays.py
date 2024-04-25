class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if nums1 == [] and nums2 == []:
            return None
        if nums1 == []:
            if len(nums2) % 2 == 0:
                return (nums2[len(nums2)//2-1] + nums2[len(nums2)//2])/2
            return nums2[len(nums2)//2]
        if nums2 == []:
            if len(nums1) % 2 == 0:
                return (nums1[len(nums1)//2-1] + nums1[len(nums1)//2])/2
            return nums1[len(nums1)//2]
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        A = nums1
        B = nums2 
        if len(A) > len(B):
            A, B = B, A 
        
        n = len(A) + len(B)
        leftA = 0 
        rightA = len(A) - 1 
        while True:
            LA = (leftA + rightA) // 2 
            RA = LA + 1 
            LB = n//2 - LA - 2
            RB = LB + 1
            vLB = B[LB] if LB >= 0 else float('-inf')
            vRB = B[RB] if RB <= len(B) - 1 else float('inf')
            vLA = A[LA] if LA >= 0 else float('-inf')
            vRA = A[RA] if RA <= len(A) - 1 else float('inf')
            
            if vLB <= vRA and vLA <= vRB:
                if n % 2:
                    return min(vRA, vRB)
                else:
                    return (max(vLA, vLB) + min(vRA, vRB)) / 2
            elif vLB > vRA:
                leftA = LA + 1 
            elif vLB <= vRA and vLA > vRB:
                rightA = LA - 1
