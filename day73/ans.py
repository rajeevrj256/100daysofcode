class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi=-1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    m=(nums[i]-1)*(nums[j]-1)
                    maxi=max(maxi,m)
        return maxi