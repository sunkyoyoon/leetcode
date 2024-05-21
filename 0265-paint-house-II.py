class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        for i in range(len(costs)):
            if i == 0:
                continue
            for j in range(len(costs[0])):
                to_add = float("inf")
                for k in range(len(costs[0])):
                    if k == j:
                        continue
                    to_add = min(to_add, costs[i-1][k])
                costs[i][j] += to_add 
        
        return min(costs[len(costs)-1])

    # O(N^2) time
    # O(1) space
