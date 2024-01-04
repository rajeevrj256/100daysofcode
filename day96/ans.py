class Solution:
    def minOperations(self, nums: List[int]) -> int:
        dictt=Counter(nums)
        ans=0
        for i in dictt:
            if dictt[i]==1:
                ans=-1
                break
            else:
                if dictt[i]%3==0:
                    ans+=dictt[i]//3
                else:
                    ans+=dictt[i]//3+1
        return ans