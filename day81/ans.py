class Solution:
    
    def buyChoco(self, prices: List[int], money: int) -> int:

        return res if (res:=money-sum(sorted(prices)[:2]))>=0 else money

        