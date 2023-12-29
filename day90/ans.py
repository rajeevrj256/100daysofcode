class Solution:
      def minDifficulty(self, arr: List[int], d: int) -> int:
    max_vals, sum_vals = [0] * len(arr), [0] * len(arr)
    max_vals[-1], sum_vals[-1] = arr[-1], arr[-1]
    for i in range(len(arr) - 2, -1, -1):
      max_vals[i] = max(max_vals[i + 1], arr[i])
      sum_vals[i] = sum_vals[i + 1] + arr[i]

    @cache
    def dp(i, d):
      if d == len(arr) - i:
        return sum_vals[i]
      if d == 1:
        return max_vals[i]

      res, curr_max = float('inf'), -1
      for j in range(i, len(arr) - d + 1):
        curr_max = max(curr_max, arr[j])
        res = min(res, curr_max + dp(j + 1, d - 1))
      return res
      
    return -1 if d > len(arr) else dp(0, d)