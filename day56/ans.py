class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        sm=sum(nums)
        l=0
        for i in range(len(nums)):
            l+=nums[i]
            nums[i]=(((i+1)*nums[i]-l)+(sm-l)-(len(nums)-i-1)*nums[i])
        return nums