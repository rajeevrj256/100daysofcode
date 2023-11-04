class Solution(object):
    def getLastMoment(self, n, left, right):
        """
        :type n: int
        :type left: List[int]
        :type right: List[int]
        :rtype: int
        """
        res = 0
        for el in left:
            res = max(res, el)
        for el in right:
            res = max(res, n - el)
        return res