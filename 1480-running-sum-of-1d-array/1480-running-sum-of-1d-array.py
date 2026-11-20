class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = 0
        l=[]
        for i in range(len(nums)):
            res+=nums[i]
            l.append(res)
        return l


             