class Solution:
      def minCost(self, colors: str, neededTime: List[int]) -> int:
    res, max_cost, sum_cost, prev = 0, 0, 0, ''
    for i in range(len(colors)):
      if colors[i] != prev:
        res += sum_cost - max_cost
        sum_cost, max_cost, prev = neededTime[i], neededTime[i], colors[i]
      else:
        sum_cost, max_cost = sum_cost + neededTime[i], max(max_cost, neededTime[i])
    
    return res + sum_cost - max_cost 