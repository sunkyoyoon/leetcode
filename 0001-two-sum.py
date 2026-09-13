from typing import List 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} 
        for i in range(len(nums)):
            num = target - nums[i]
            if num in hashmap:
                return [hashmap[num], i]
            hashmap[nums[i]] = i 

        hashmap[nums[i]] = i 
        
if __name__ == "__main__":
    sol = Solution()

    # Define test cases: (nums, target, expected_output)
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-1, -2, -3, -4, -5], -8, [2, 4])
    ]

    # Run and validate test cases
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        print(i)
        result = sol.twoSum(nums, target)
        status = "PASSED" if result == expected else f"FAILED (Expected {expected}, got {result})"
        print(f"Test Case {i}: nums={nums}, target={target} -> Result: {result} | {status}")