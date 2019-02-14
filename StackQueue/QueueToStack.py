class MyStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.count = 0

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.count += 1
        self.queue.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.count > 0:
            for i in range(self.count - 1):
                self.queue.append(self.queue.pop(0))
            self.count -= 1
            return self.queue.pop[0]
        else:
            return None

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.count > 0:
            for i in range(self.count - 1):
                self.queue.append(self.queue.pop(0))
            top = self.queue[0]
            self.queue.append(self.queue.pop(0))
            return top
        else:
            return None

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.count == 0