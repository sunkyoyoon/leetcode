class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks = Counter(tasks)
        heap = [-cnt for cnt in tasks.values()]
        heapify(heap)
        q = deque()
        time = 0 

        while heap or q:
            time += 1 
            if heap:
                cnt = -heappop(heap)
                cnt -= 1 
                if cnt > 0:
                    q.append((cnt, time + n))

            if q:        
                cnt, t = q[0]
                if t <= time:
                    cnt, _ = q.popleft()
                    heappush(heap, -cnt)

        return time



