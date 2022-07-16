class Solution:
    def twoSum(self, nums, target):
        d={}
        for i,v in enumerate(nums):
            dif=target-v
            if dif in d:
                return [d[dif],i]
            d[v]=i