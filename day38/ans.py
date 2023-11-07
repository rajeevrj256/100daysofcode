class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time =[]
        for i in range(len(dist)):
            time.append(dist[i]/speed[i])

        time.sort()
        count=0
        t=0
        for i in range(len(dist)):
            if i>=time[i]:
                i-=1
                break

        return i+1
