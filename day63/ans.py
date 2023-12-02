class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counts =[0]*26
        for ch in chars:
            counts[ord(ch)-ord('a')]+=1
        
        ans=0
        def wordform(word,counts):
            c=[0]*26
            for ch in word:
                x=ord(ch)-ord('a')
                c[x]+=1
                if c[x]>counts[x]:
                    return False
            return True
        for word in words:
            if wordform(word,counts):
                ans+=len(word)
        return ans