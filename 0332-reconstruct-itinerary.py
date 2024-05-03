class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {} 
        for t in tickets:
            if t[0] not in adj:
                adj[t[0]] = []
            if t[1] not in adj:
                adj[t[1]] = [] 
            adj[t[0]].append(t[1])

        for t in adj:
            adj[t].sort(reverse = True) 
        
        stack = ["JFK"]
        res = []
        while stack:
            ticket = stack[-1]
            if ticket not in adj or adj[ticket] == []:
                res.append(stack.pop())
            else:
                stack.append(adj[ticket].pop())

        return res[::-1]
