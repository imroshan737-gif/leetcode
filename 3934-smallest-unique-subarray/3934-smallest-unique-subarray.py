class Solution(object):
    def smallestUniqueSubarray(self, nums):
        n = len(nums)
        mod1, mod2 = 1000000007, 1000000009
        base = 131

        p1 = [1] * (n + 1)
        p2 = [1] * (n + 1)
        h1 = [0] * (n + 1)
        h2 = [0] * (n + 1)

        for i in range(n):
            p1[i + 1] = p1[i] * base % mod1
            p2[i + 1] = p2[i] * base % mod2
            h1[i + 1] = (h1[i] * base + nums[i]) % mod1
            h2[i + 1] = (h2[i] * base + nums[i]) % mod2

        def check(length):
            seen = {}
            single = 0

            for i in range(n - length + 1):
                a = (h1[i + length] - h1[i] * p1[length]) % mod1
                b = (h2[i + length] - h2[i] * p2[length]) % mod2
                key = a * mod2 + b

                count = seen.get(key, 0)

                if count == 0:
                    single += 1
                elif count == 1:
                    single -= 1

                seen[key] = count + 1

            return single > 0

        left, right = 1, n

        while left < right:
            mid = (left + right) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left
        