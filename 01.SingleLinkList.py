class Node:
    """节点"""
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SingleLinkList:
    """单向链表"""
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """判断是否为空"""
        # 返回头节点是否为空
        return self.__head is None

    def length(self):
        """返回长度"""
        # 遍历所有节点
        count = 0
        curr_node = self.__head
        while curr_node:
            count += 1
            curr_node = curr_node.next
        return count

    def travel(self):
        """遍历输出元素"""
        # 遍历所有节点
        if self.is_empty():
            print('单向链表为空')
        else:
            curr_node = self.__head
            while curr_node:
                print(curr_node.data, end=" ")
                curr_node = curr_node.next
            print('')

    def add(self, item):
        """头部插入元素"""
        # 先将插入的节点指向第一个节点,再讲头节点指向插入的节点
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """尾部插入元素"""
        # 遍历所有节点, 将尾结点指向新插入的节点
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            curr_node = self.__head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = node

    def insert(self, index, item):
        """指定位置插入元素"""
        # 若index小于等于0, 则认为是从头部插
        if index <= 0:
            self.add(item)
        # 若index大于等于链表长度, 则认为是从尾部插
        elif index >= self.length():
            self.append(item)
        # 其他情况为中间插入
        else:
            node = Node(item)
            count = 0
            curr_node = self.__head
            while count + 1 < index:
                curr_node = curr_node.next
                count += 1
                # a b c index=1
            node.next = curr_node.next
            curr_node.next = node

    def remove(self, item):
        """删除第一个item元素"""
        if self.is_empty():
            print('单向链表为空')
        else:
            curr_node = self.__head
            # 当起始元素就是需要删除的元素时
            if curr_node.data == item:
                self.__head = curr_node.next
            else:
                while curr_node.next.data != item:
                    curr_node = curr_node.next
                    # 考虑已经遍历完的情况
                    if not curr_node.next:
                        print('链表中无该元素')
                        return
                curr_node.next = curr_node.next.next

    def search(self, item):
        """查询元素是否存在, 返回下标"""
        if self.is_empty():
            return None
        count = 0
        curr_node = self.__head
        while curr_node.data != item:
            curr_node = curr_node.next
            if not curr_node.next:
                return None
            count += 1
        return count


if __name__ == '__main__':
    singlelinklist = SingleLinkList()
    print(singlelinklist.is_empty())
    singlelinklist.add('a')
    print(singlelinklist.is_empty())
    singlelinklist.travel()
    singlelinklist.append('b')
    singlelinklist.append('c')
    singlelinklist.append('d')
    singlelinklist.append('e')
    singlelinklist.append('f')
    singlelinklist.travel()
    print(singlelinklist.length())
    singlelinklist.insert(2, 'A')
    singlelinklist.travel()
    singlelinklist.add('b')
    singlelinklist.travel()
    singlelinklist.remove('e')
    singlelinklist.travel()
    print(singlelinklist.search('A'))
