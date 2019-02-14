class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.queue:
            num = len(self.queue)
            for _ in range(num - 1):
                self.queue.append(self.queue.pop(0))
            return self.queue.pop(0)
        else:
            return None


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.queue:
            num = len(self.queue)
            for _ in range(num - 1):
                self.queue.append(self.queue.pop(0))
            res = self.queue[0]
            self.queue.append(self.queue.pop(0))
            return res
        else:
            return None

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.queue

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


import collections
class MyStackV1(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = collections.deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)
        num = len(self.queue)
        for _ in range(num-1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.queue:
            return self.queue.popleft()
        else:
            return None


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.queue:
            return self.queue[0]
        else:
            return None

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.queue

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
