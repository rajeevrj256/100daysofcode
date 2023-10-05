class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x=[]
        y=[]

        for i in nums:
            if i not in x:
                x.append(i)
        for i in x:
             if nums.count(i) > (len(nums)/3):
                     y.append(i)
               
        return y