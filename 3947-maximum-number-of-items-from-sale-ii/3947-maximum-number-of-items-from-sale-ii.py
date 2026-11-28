class Solution(object):
    def maximumSaleItems(self, items, budget):
        n = len(items)
        freq = [0] * (n + 1)

        for f, p in items:
            freq[f] += 1

        gain = [0] * (n + 1)
        for f in range(1, n + 1):
            for x in range(f, n + 1, f):
                gain[f] += freq[x]
            gain[f] -= 1

        q = min(p for f, p in items)
        items.sort(key=lambda x: x[1])

        boosted = 0

        for f, p in items:
            if p > 2 * q or budget < p:
                break

            take = min(gain[f], budget // p)
            boosted += take
            budget -= take * p

            if take < gain[f]:
                break

        return boosted * 2 + budget // q