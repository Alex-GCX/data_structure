class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """队尾加入元素, 入队"""
        self.items.append(item)

    def dequeue(self):
        """对头弹出元素, 出队"""
        return self.items.pop(0)

    def is_empty(self):
        """返回是否为空"""
        return len(self.items) == 0

    def size(self):
        """返回队列大小"""
        return len(self.items)

    def traval(self):
        """遍历队列"""
        return self.items


if __name__ == '__main__':
    queue = Queue()
    print(queue.is_empty())
    queue.enqueue('a')
    queue.enqueue('b')
    queue.enqueue('c')
    queue.enqueue('d')
    queue.enqueue('e')
    print(queue.is_empty())
    print(queue.traval())
    print(queue.dequeue())
    print(queue.traval())
    print(queue.size())
