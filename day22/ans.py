class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        if n==1:
            return nums[0]
        minN=nums[k]
        i=k
        j=k
        ans=-sys.maxsize-1
        while(i>0 or j<n-1):
            if (i==0): 
                j+=1
            elif j==n-1:
                i-=1
            elif nums[i-1]<nums[j+1]:
                j+=1
            else:
                 i-=1
            minN=min(minN,nums[i],nums[j])
            ans=max(ans,minN*(j-i+1))
        return ans