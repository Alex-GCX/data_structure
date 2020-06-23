class Stack:
    """栈"""
    def __init__(self):
        """构造空列表"""
        self.items = []

    def push(self, item):
        """栈顶插入元素, 入栈, 压栈"""
        self.items.append(item)

    def pop(self):
        """弹出栈顶元素, 出栈"""
        return self.items.pop(-1)

    def peek(self):
        """返回栈顶元素, 不弹出"""
        return self.items[-1]

    def is_empty(self):
        """返回是否为空"""
        return len(self.items) == 0

    def size(self):
        """返回大小"""
        return len(self.items)

    def traval(self):
        """遍历栈"""
        print(self.items)


if __name__ == "__main__":
    stack = Stack()
    print(stack.is_empty())
    stack.push('a')
    stack.push('b')
    stack.push('c')
    stack.push('d')
    stack.traval()
    print(stack.pop())
    print(stack.peek())
    stack.traval()
    print(stack.is_empty())
    print(stack.size())
