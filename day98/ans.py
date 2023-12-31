class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])  
        dp = [(0, 0)] 
        
        for s, e, p in jobs:
            
            idx = bisect.bisect_right(dp, (s, float('inf'))) - 1
            curr_profit = dp[idx][1] + p
            dp.append((e, max(curr_profit, dp[-1][1])))
        
        return dp[-1][1] 