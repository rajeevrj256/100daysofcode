class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==0: return False
        return n==1 or (n%4==0 and self.isPowerOfFour(n//4)) 
        