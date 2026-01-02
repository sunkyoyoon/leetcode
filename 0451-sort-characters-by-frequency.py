class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        ans = ""
        a = sorted(cnt, key=lambda x : cnt[x])
        for c in a:
            for _ in range(cnt[c]):
                ans += c
        return ans[::-1]
