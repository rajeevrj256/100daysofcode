class Solution(object):
    def minimumTime(self, n, relations, time):
        """
        :type n: int
        :type relations: List[List[int]]
        :type time: List[int]
        :rtype: int
        """
        graph = collections.defaultdict(list)
        in_degree = [0] * n
        
        for prev, nextt in relations:
            graph[prev - 1].append(nextt - 1)
            in_degree[nextt - 1] += 1
        
    
        heap = [(time[i], i) for i in range(n) if in_degree[i] == 0]
        heapq.heapify(heap)
        
        
        result = 0
        processed_nodes = 0
        
        while heap:
            m, node = heapq.heappop(heap)
            result = max(result, m)
            processed_nodes += 1
            
            for nextt in graph[node]:
                in_degree[nextt] -= 1
                if in_degree[nextt] == 0:
                    heapq.heappush(heap, (m + time[nextt], nextt))
        
       
        if processed_nodes == n:
            return result
        else:
            return -1  