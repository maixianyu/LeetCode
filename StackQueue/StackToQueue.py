class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stackInput = []
        self.stackOutput = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stackInput.append(x)


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.stackOutput) == 0 :
            for i in range(len(self.stackInput)):
                self.stackOutput.append(self.stackInput.pop())

        if len(self.stackOutput) != 0:
            return self.stackOutput.pop()
        else:
            return None


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.stackOutput) == 0:
            for i in range(len(self.stackInput)):
                self.stackOutput.append(self.stackInput.pop())

        if len(self.stackOutput) != 0:
            return self.stackOutput[-1]
        else:
            return None

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return (len(self.stackInput) == 0) and (len(self.stackOutput) == 0)
