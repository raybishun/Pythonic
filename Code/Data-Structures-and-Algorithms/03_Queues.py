class Queue:
    def __init__(self):
        self.queue = list()
        self.first = -1
        self.last = -1

    def enqueue(self, value):
        if self.first == -1:
            self.first = self.first + 1

        self.last = self.last + 1
        self.queue.insert(self.last, value)

my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(3)
my_queue.enqueue(5)

print(my_queue.queue)