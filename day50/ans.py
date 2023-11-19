from typing import List

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        count = 0
        
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                count += 1  
        
            ans += count  
        
        return ans
