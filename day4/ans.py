class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s[::-1]
        rev=s.split(" ")
        rev =rev[::-1]
        r=" ".join(rev)

        return r
        