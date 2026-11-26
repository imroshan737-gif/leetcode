class Solution(object):
    def canAliceWin(self, n):
        stones = 10
        turns = 0

        while n >= stones:
            n -= stones
            stones -= 1
            turns += 1

        return turns % 2 == 1