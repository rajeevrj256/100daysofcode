class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort( key=lambda k: [k[0], k[1]])
        maxi=0
        for i in range(1,len(points)):
            maxi=max(maxi,(points[i][0]-points[i-1][0]))
        return maxi



        