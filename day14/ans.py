class Solution(object):
    def paintWalls(self, cost, time):
        """
        :type cost: List[int]
        :type time: List[int]
        :rtype: int
        """
        n= len(cost)
        dp=[float('inf')]*(n+1)
        dp[0]=0
        for i in range(n):
            for j in range(n,0,-1):
                dp[j] = min(dp[j] , dp[max(j-time[i]-1,0)] + cost[i])

            
        return dp[n]


        