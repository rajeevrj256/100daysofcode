class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        n = len(arr)
        if k == 1:
            return max(arr[0], arr[1])

        winner = arr[0]
        consecutive_wins = 0

        for i in range(1, n):
            if arr[i] > winner:
                winner = arr[i]
                consecutive_wins = 1
            else:
                consecutive_wins += 1

            if consecutive_wins == k:
                break

        return winner


