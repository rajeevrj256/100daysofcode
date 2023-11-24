class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n=len(piles)

        a=n//3
        r=a
        ans=0
        for i in range(a):
            ans+=piles[r]
            r+=2

        return ans




        