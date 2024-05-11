class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 0:
            return 
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost)
        
        for i in range(2,len(cost)):
            cost[i] = cost[i] + min(cost[i-2],cost[i-1])
        
        return min(cost[len(cost)-1], cost[len(cost)-2])
