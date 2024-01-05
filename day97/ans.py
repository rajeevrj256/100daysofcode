class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans=0
        arr=[1]*len(nums)
        for i in range (len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    arr[i]=max(arr[i],arr[j]+1)
            ans=max(ans,arr[i])
            
        return ans




        