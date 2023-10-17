class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """
        graph = defaultdict(list)
        in_degree = [0] * n

        for node in range(n):
            left, right = leftChild[node], rightChild[node]
            if left != -1:
                graph[node].append(left)
                in_degree[left] += 1
            if right != -1:
                graph[node].append(right)
                in_degree[right] += 1

        root_candidates = set(range(n)) - set(node for node in range(n) if in_degree[node] > 0)

        if len(root_candidates) != 1:
            return False
        root = root_candidates.pop()

        queue = deque([root])
        seen = set([root])

        while queue:
            node = queue.popleft()
            if node in graph:
                for child in graph[node]:
                    if child in seen:
                        return False
                    seen.add(child)
                    queue.append(child)

        return len(seen) == n




