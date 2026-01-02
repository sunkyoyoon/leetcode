class Solution:
    def alertNames(self, keyName, keyTime):
        ans = set()
        hashmap = defaultdict(deque)

        for name, t in sorted(zip(keyName, keyTime)):
            h, m = map(int, t.split(":"))
            time = h * 60 + m
            a = hashmap[name]
            while a and time - a[0] > 60:
                a.popleft()
            a.append(time)

            if len(a) >= 3:
                ans.add(name)
        
        return sorted(ans)
