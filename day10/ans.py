class Solution:
    
    def minOperations(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        n=len(nums)
        s=set(nums)
        s=list(s)
        s.sort()
        maax=0
        for i in range(len(s)-1):
            lo=i
            hi=len(s)-1
            ans=-1
            target=s[i]+n-1
            while lo<=hi:
                mid=(lo+hi)//2
                if s[mid]<=target:
                    ans=mid
                    lo=mid+1
                else:
                    hi=mid-1
            maax=max(maax,ans-i+1)
        return n-maax

