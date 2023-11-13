class Solution:
    def sortVowels(self, s: str) -> str:
        l = list(s)
        vowelsCntr = dict(map(lambda x: (x, 0), 'AEIOUaeiou'))
        for ch in l:
            if ch in vowelsCntr:
                vowelsCntr[ch] += 1

        it = iter(vowelsCntr)
        curCh = next(it)
        for i, ch in enumerate(l):
            if ch in vowelsCntr:
                while vowelsCntr[curCh] == 0:
                    curCh = next(it)
                l[i] = curCh
                vowelsCntr[curCh] -= 1

        return ''.join(l)