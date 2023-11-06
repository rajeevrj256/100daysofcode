import Queue
class SeatManager(object):
    

    def __init__(self, n):
        """
        :type n: int
        """
        self.seat=Queue.PriorityQueue()

        for i in range(n):
            self.seat.put(i+1)

        

    def reserve(self):
        """
        :rtype: int
        """
        return self.seat.get()
        
        

    def unreserve(self, seatNumber):
        """
        :type seatNumber: int
        :rtype: None
        """
        self.seat.put(seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)