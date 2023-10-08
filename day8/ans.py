class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        s=len(nums1)
        t=len(nums2)
        L = [[float('-inf')]*(t+1) for _ in range(s+1)]
        for i in range(s+1):
            for j in range(t+1):
                if i==0 or j==0:
                    L[i][j]= float('-inf')
                else:
                    L[i][j]=max(nums1[i-1]*nums2[j-1]+max(L[i-1][j-1],0),max(L[i-1][j],L[i][j-1]))
        return L[s][t]
        