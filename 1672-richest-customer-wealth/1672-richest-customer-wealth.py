class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        # m=0
        # a=0
        # for i in accounts:
        #     a=sum(i)
        #     m=max(m,a)
        # return m
        return max(sum(i) for i in accounts)
               