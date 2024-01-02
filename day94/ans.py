class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        dictt = defaultdict(int)
        for num in nums:
            dictt[num]+=1
        ans=[]
        while dictt:
            temp=[]
            for num, value in list(dictt.items()):
                temp.append(num)
                dictt[num]-=1
                if dictt[num]==0:
                    del dictt[num]
            ans.append(temp)

        return ans
        

