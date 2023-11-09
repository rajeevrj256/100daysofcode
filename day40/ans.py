class Solution:
    def countHomogenous(self, s: str) -> int:
        left =0
        an=0
        for right in range(len(s)):
            if s[left]==s[right]:
                an+=right-left +1
            else:
                an+=1
                left=right
        return an % (10**9 + 7)