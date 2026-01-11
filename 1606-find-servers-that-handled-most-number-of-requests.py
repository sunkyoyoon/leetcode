class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        # available sorted list of free server ids
        free = SortedList(range(k))
        # busy min-heap, stores (end_time, server_id)
        busy = []
        # count how many requests each server handled
        cnt = [0] * k

        for i, (start, t) in enumerate(zip(arrival, load)):
            # free up all servers whose work ended before this arrival
            while busy and busy[0][0] <= start:
                end_time, sid = heappop(busy)
                free.add(sid)

            # if no server is free now, drop the request
            if not free:
                continue

            # find index in free ≥ (i % k)
            idx = free.bisect_left(i % k)
            if idx == len(free):  # wrap-around
                idx = 0

            server = free.pop(idx)   # assign this server
            cnt[server] += 1
            heappush(busy, (start + t, server))

        # find the max count and return all servers with that count
        mx = max(cnt)
        return [i for i, v in enumerate(cnt) if v == mx]

