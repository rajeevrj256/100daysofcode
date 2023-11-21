from collections import defaultdict

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        reverse_diff_count = defaultdict(int)
        ans = 0
        
        for num in nums:
            # Calculate the difference between the number and its reverse
            reverse_diff = num - int(str(num)[::-1])
            ans = (ans + reverse_diff_count[reverse_diff]) % mod
            reverse_diff_count[reverse_diff] += 1
        
        return ans
