class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        cnt, res = [0] * (n + 1), [0] * len(queries)
        shared = Counter()
        for u, v in edges:
            cnt[u] += 1
            cnt[v] += 1
            if u < v:
                shared[(u,v)] += 1 
            else:
                shared[(v,u)] += 1 

        sorted_cnt = sorted(cnt[1:])

        for qi, q in enumerate(queries):
            total = 0 

            j = n - 1 
            for i in range(n):
                while j > i and sorted_cnt[i] + sorted_cnt[j] > q:
                    j -= 1 
                total += n - 1 - max(j,i)
            
            for (u,v), c in shared.items():
                if cnt[u] + cnt[v] > q and cnt[u] + cnt[v] - c <= q:
                    total -= 1 
            res[qi] = total 
        
        return res


        
