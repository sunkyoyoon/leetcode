class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        res = []  
        for i, v in enumerate(nums):
            while queue and (queue[-1][0] < nums[i] or i - queue[-1][1] + 1 > k):
                queue.pop()
            while queue and i - queue[0][1] + 1 > k:
                queue.popleft()
            queue.append((v,i))
            if i + 1 >= k:
                res.append(queue[0][0])
        return res


