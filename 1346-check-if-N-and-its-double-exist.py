class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hashmap = defaultdict(list)
        for i in range(len(arr)):
            hashmap[arr[i]].append(i) 
        for i in range(len(arr)):
            n = arr[i]
            if 2 * n in hashmap and any(i != x for x in hashmap[2*n]):
                return True
        
        return False 
