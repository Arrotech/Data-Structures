class Queue:
    def __init__(self, items=[]):
        self.items = items

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def rear(self):
        return self.items[-1]

    def front(self):
        return self.items[0]

if __name__ == '__main__':

    queue = Queue()
    print(queue.isEmpty())
    queue.enqueue("a")
    queue.enqueue("b")
    queue.enqueue("c")
    queue.enqueue("d")
    queue.enqueue("e")
    queue.dequeue()
    queue.dequeue()
    print(queue.rear())
    print(queue.front())
    print(queue.isEmpty())
    print(queue.size())