class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def arithmetic(nums):
            nums.sort()
            ans=nums[1]-nums[0]
            for i in range(1,len(nums)):
                anss=nums[i]-nums[i-1]
                if anss!=ans:
                    return False
            return True
        res=[]
        for i in range(len(l)):
            arr=nums[l[i]:r[i]+1]
            res.append(arithmetic(arr))

        return res     
                

        