class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_sum=0
        n=len(nums)
        l,r=0,n-1
        while l<r:
            max_pair=nums[l]+nums[r]
            max_sum=max(max_sum,max_pair)
            l+=1
            r-=1
        return max_sum
