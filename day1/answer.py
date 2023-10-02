class Solution(object):
    def winnerOfGame(self, colors):
        """
        :type colors: str
        :rtype: bool
        """
        if len(colors)<=2:
            return False
        acount=0
        bcount=0
        n=len(colors)

        for i in range(1,n-1):
            if colors[i - 1] == 'A' and colors[i] == 'A' and colors[i + 1] == 'A':
               acount=acount+1
            if colors[i-1] == 'B' and colors[i] == 'B' and colors[i+1] == 'B':
                bcount=bcount+1

        
        return acount>bcount
        