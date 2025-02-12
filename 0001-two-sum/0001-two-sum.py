from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for param_1 in range(n-1):
            for param_2 in range(param_1+1,n):
               if param_2!=param_1:
                 if nums[param_1]+ nums[param_2] == target:
                     return [param_1,param_2]
        return[]             
