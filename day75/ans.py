class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row=len(grid)
        col=len(grid[0])
        diff = [[0 for _ in range(col)] for _ in range(row)]
        onesrow=[0]*row
        onescol=[0]*col
        zerorow=[0]*row
        zerocol=[0]*col
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    onesrow[i]+=1
                    onescol[j]+=1
                else:
                    zerorow[i]+=1
                    zerocol[j]+=1
        
        for i in range(row):
            for j in range(col):
                diff[i][j]=onesrow[i]+onescol[j]-zerorow[i]-zerocol[j]
        
        return diff

