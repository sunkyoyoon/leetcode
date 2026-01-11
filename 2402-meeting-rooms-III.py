class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort() 
        available = [i for i in range(n)]
        heapify(available)
        counter = [0] * n 

        heap = [] 
        for start, end in meetings:
            while heap and start >= heap[0][0]:
                _,room = heappop(heap)
                heappush(available, room)

            if available:
                room = heappop(available)
                heappush(heap, (end, room))
            else:
                e, room = heappop(heap)
                heappush(heap, (e + end - start, room))
            counter[room] += 1 

        return counter.index(max(counter))

