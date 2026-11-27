class Solution(object):
    def maximumSaleItems(self, items, budget):
        n = len(items)
        bonus = [0] * n

        for i in range(n):
            f = items[i][0]
            for j in range(n):
                if i != j and items[j][0] % f == 0:
                    bonus[i] += 1

        dp = [0] * (budget + 1)

        for i in range(n):
            p = items[i][1]
            v = bonus[i]
            curr = dp[:]

            for r in range(p):
                best = -1
                t = 0

                for b in range(r, budget + 1, p):
                    if t > 0:
                        prev = dp[b - p]
                        if prev >= 0:
                            best = max(best, prev - (t - 1))

                    if best >= 0:
                        curr[b] = max(curr[b], best + t + v)

                    t += 1

            dp = curr

        return max(dp)