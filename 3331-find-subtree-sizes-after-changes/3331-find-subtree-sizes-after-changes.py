class Solution(object):
    def findSubtreeSizes(self, parent, s):
        n = len(parent)
        adj = [[] for _ in range(n)]

        for i in range(1, n):
            adj[parent[i]].append(i)

        newParent = parent[:]
        last = [-1] * 26

        def dfs(node):
            c = ord(s[node]) - ord('a')
            prev = last[c]

            if node != 0 and prev != -1:
                newParent[node] = prev

            last[c] = node

            for child in adj[node]:
                dfs(child)

            last[c] = prev

        dfs(0)

        newAdj = [[] for _ in range(n)]

        for i in range(1, n):
            newAdj[newParent[i]].append(i)

        ans = [0] * n

        def calc(node):
            ans[node] = 1

            for child in newAdj[node]:
                ans[node] += calc(child)

            return ans[node]

        calc(0)
        return ans