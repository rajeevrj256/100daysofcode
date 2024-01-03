class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        arrayss = [list(string) for string in bank if any(char != '0' for char in string)]
        arr=[]
        for i in range (len(arrayss)):
            count=0
            for j in range (len(arrayss[i])):
                if arrayss[i][j]=='1':
                    count+=1
            arr.append(count)
        sum=0
        for i in range(1,len(arr)):
            prd=arr[i-1]*arr[i]
            sum+=prd
        return sum
