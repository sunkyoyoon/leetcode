class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        walls.sort()
        def lower_bound(arr, x):
            """Return the first index i where arr[i] >= x."""
            lo, hi = 0, len(arr)
            while lo < hi:
                mid = (lo + hi) // 2
                if arr[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo


        def upper_bound(arr, x):
            """Return the first index i where arr[i] > x."""
            lo, hi = 0, len(arr)
            while lo < hi:
                mid = (lo + hi) // 2
                if arr[mid] <= x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo


        def count(L, R):
            """Count number of walls w where L <= w <= R."""
            if L > R:
                return 0
            li = lower_bound(walls, L)
            ri = upper_bound(walls, R)
            return ri - li

        A = sorted(zip(robots, distance))
        A.append([inf, 0])
        avail = 0 
        used = count(A[0][0] - A[0][1], A[0][0] - 1)
        for i in range(len(A)-1):
            l, dl = A[i]
            r, dr = A[i + 1]

            l1, r1 = l + 1, min(l + dl, r - 1)
            l2, r2 = max(l+1, r - dr), r - 1

            left = count(l1,r1)
            right = count(l2,r2)
            both = left + right - count(max(l1, l2), min(r1, r2))

            navail = max(used, left + avail)
            nused = max(used+right, both+avail)

            avail = navail
            used = nused
        
        for x in set(x for x,_ in A):
            used += count(x,x)
        return used


