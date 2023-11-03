class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        result = []
        counter = 0
        for i in range(1, n + 1):
            if i in target:
                while counter > 0:
                    result.append("Pop")
                    counter -= 1
            else:
                counter += 1
            result.append("Push")

            if i == target[-1]:
                break

        return result

        