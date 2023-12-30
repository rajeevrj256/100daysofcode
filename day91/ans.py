class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        if len(words)==1:
            return True
        tot_char_count=sum(len(i) for i in words )

        if tot_char_count%len(words)!=0:
            return False
        
        mapp=[0]*26
        for s in words:
            for ch in s:
                mapp[ord(ch)-ord('a')]+=1
        
        for i in mapp:
            if i%len(words)!=0:
                return False
        
        return True


