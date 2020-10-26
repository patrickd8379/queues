class linQ:
    def __init__(self):
        self.empty = True
        self.queue = []
        self.length = 5
        self.head = -1
        self.tail = -1
        for i in range(self.length):
            self.queue.append([])
    def addToLinQ(self, value):
        if self.tail == self.length:
            return "Queue is full"
        else:
            self.queue[self.head + 1] = value
            if self.empty:
                self.head += 1
                self.empty = False
            self.tail += 1
            return self.queue
    def deQLinQ(self):
        if self.empty:
            return "Queue is Empty"
        else:
            print(self.queue[self.tail])
            self.queue[self.tail] = []
            self.tail -= 1
            if self.tail == -1:
                self.head = -1
                self.empty = True
            return self.queue

linearQueue = linQ()
linearQueue.addToLinQ("Hello")
linearQueue.addToLinQ("There")
linearQueue.deQLinQ()
print(linearQueue.queue)
