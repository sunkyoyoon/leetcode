class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [] 
        arr2 = [] 
        for n in nums:
            if arr1 == []:
                arr1.append(n)
            elif arr2 == []:
                arr2.append(n)
            else:
                if arr1[-1] >= arr2[-1]:
                    arr1.append(n)
                else:
                    arr2.append(n)

        return arr1 + arr2
            

