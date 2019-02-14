class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stackIn = []
        self.stackOut = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stackIn.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.stackOut:
            return self.stackOut.pop()
        else:
            while self.stackIn:
                self.stackOut.append(self.stackIn.pop())
            if self.stackOut:
                return self.stackOut.pop()
            else:
                return None


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.stackOut:
            return self.stackOut[-1]
        else:
            while self.stackIn:
                self.stackOut.append(self.stackIn.pop())
            if self.stackOut:
                return self.stackOut[-1]
            else:
                return None

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.stackIn and not self.stackOut

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()