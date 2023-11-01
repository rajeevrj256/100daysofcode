class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        n= len(pref)
        if n < 2:
            return pref
        arr=list(pref)
        app= pref[0]^ pref[1]
        for i in range(1,n):
           arr[i]=pref[i-1]^pref[i]
            
        
        return arr

        