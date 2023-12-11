class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dictt={key: 0 for key in set(arr)}
        ans=0
        for i in arr:
            
            
            dictt[i]+=1
            if (dictt[i]/len(arr))*100>25:
                return i

        return -1


        