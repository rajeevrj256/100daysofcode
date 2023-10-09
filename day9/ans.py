class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s=[]
        
        y=0
        count=0
        for i in range(len(nums)):
            if count==0:
                if nums[i]==target:
                    y=i
                    count=1
            
            if nums[i]==target:
                s.append(i)

        if s:
            x=s.pop()
        else:
            x=-1
        
        if count==0:
            return [-1,-1]
        else:
            return [y,x]

        

        