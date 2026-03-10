class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        last_position = {}
        deleted_indices = set()
        for i in range(len(s)):
            if s[i] in last_position and i - last_position[s[i]] <= k:
                deleted_indices.add(i)
                for j in last_position:
                    last_position[j] += 1 

            else:
                
                last_position[s[i]] = i

        result = "".join(c for i, c in enumerate(s) if i not in deleted_indices)
        
        return result


