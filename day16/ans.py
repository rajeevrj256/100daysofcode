class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        n=rowIndex
        res=[]
        s=1
        res.append(s)
        for i in range(n):
            s *= (n-i)
            s //= (i+1)
            res.append(s)
        return res