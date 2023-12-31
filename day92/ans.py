class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        n=len(s)
        ans=-1
        for i in range(n):
            for j in range(n-1,0,-1):
                if s[i]==s[j]:
                    ans=max(ans,j-i-1)
        return ans