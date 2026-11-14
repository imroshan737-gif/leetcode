class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        ans = float('inf')

        for i in range(len(nums)):
            total = 0

            for j in range(i, len(nums)):
                total += nums[j]
                length = j - i + 1

                if length >= l and length <= r:
                    if total > 0 and total < ans:
                        ans = total

                if length == r:
                    break

        if ans == float('inf'):
            return -1

        return ans