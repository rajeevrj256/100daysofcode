class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        monday = 1

        for i in range(n):
            if i % 7 == 0:
                monday = (i // 7) + 1
            ans += monday + (i % 7) 
        return ans
