class Solution:
    def canAliceWin(self, n: int) -> bool:
        r = 10
        a = True
        while n >=r:
            n-=r
            r-=1
            a = not a
        return not a