class Solution(object):
    def numWays(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """
        n = min(steps//2+1,arrLen)
        m= steps
        dp = [[0]*n for i in range(m+1)]
        dp[0][0]=1
        mod = 10**9+7
        for i in range(1,m+1):
            for j in range(n):
                dp[i][j]=dp[i-1][j]
                if j>0:
                    dp[i][j] +=dp[i-1][j-1]
                if j<n-1:
                    dp[i][j]+=dp[i-1][j+1]
        return dp[m][0]%mod


        