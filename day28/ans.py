class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev, mod = [1, 1, 1, 1, 1], 10**9 + 7
        for _ in range(n - 1):
            prev = [
              (prev[1] + prev[2] + prev[4]) % mod,(prev[0] + prev[2]) % mod,(prev[1] + prev[3]) % mod,prev[2],(prev[2] + prev[3])% mod ]
    
        return sum(prev) % mod
        
        