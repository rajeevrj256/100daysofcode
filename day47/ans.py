class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums)
        ans=""
        for i in range(n):
            ans+='1'if nums[i][i]=='0' else '0'
        return ans
        

        