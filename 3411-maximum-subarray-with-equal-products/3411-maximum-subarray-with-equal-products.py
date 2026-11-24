class Solution(object):
    def maxLength(self, nums):
        n = len(nums)
        ans = 1

        for i in range(n):
            p = 1
            g = 0
            l = 1

            for j in range(i, n):
                x = nums[j]
                p *= x

                a, b = g, x
                while b:
                    a, b = b, a % b
                g = a

                a, b = l, x
                while b:
                    a, b = b, a % b
                l = l * x // a

                if p == g * l:
                    ans = max(ans, j - i + 1)

        return ans