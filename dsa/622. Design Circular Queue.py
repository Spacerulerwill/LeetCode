# https://leetcode.com/problems/design-circular-queue/description/

class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0 for i in range(k)]
        self.max_size = k
        self.front = -1
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = 0
        self.rear += 1
        if self.rear == self.max_size:
            self.rear = 0
        self.queue[self.rear] = value
        return True
        
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queue[self.front] = 0
        if self.front == self.rear:
            self.front = -1
            self.rear = - 1
        elif self.front == self.max_size - 1:
            self.front = 0
        else:
            self.front += 1
        return True
        
    def Front(self) -> int:
        return self.queue[self.front]

    def Rear(self) -> int:
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.front == -1

    def isFull(self) -> bool:
        return (self.front == 0 and self.rear == self.max_size - 1) or (self.rear + 1) % self.max_size == self.front

if __name__ == "__main__":
    obj = MyCircularQueue(5)
    obj.enQueue(5)
    obj.enQueue(5)
    obj.enQueue(5)
    print(obj.queue)
    obj.deQueue()
    obj.deQueue()
    obj.deQueue()
    print(obj.queue)
    