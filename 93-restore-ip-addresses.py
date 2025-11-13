class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def backtrack(start, parts):
            if len(parts) == 4 :
                if start == len(s):
                    ans.append(".".join(parts.copy()))
                else:
                    return 

            for j in range(start,min(start+3, len(s))):
                segment = s[start:j+1]
                if len(segment) > 1 and segment[0] == "0":
                    continue
                if int(segment) > 255:
                    continue
                parts.append(segment)
                backtrack(j+1,parts)
                parts.pop()

        backtrack(0, [])
        return ans


