import math
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            p = 1
            g = 0
            l = 1
            for j in range(i,len(nums)):
                x = nums[j]
                p = p*x
                g = math.gcd(g,x)
                l = math.lcm(l,x)
                if p == l * g:
                    ans = max(ans,j-i+1)
        return ans

 

                







       