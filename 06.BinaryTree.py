class Node:
    """节点"""
    def __init__(self, data=None, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child


class BinaryTree:
    """二叉树"""
    def __init__(self, root=None):
        self.root = root

    def add(self, data):
        """添加节点(广度优先遍历)"""
        # 构造需要添加的新节点
        node = Node(data)
        # 若根节点就是空, 则将新节点置为根节点
        if self.root is None:
            self.root = node
            return
        # 构造节点处理队列, 广度优先遍历, 即按从上到下,从左到右遍历节点
        # 弹出需要处理的节点, 若该节点有子节点, 则将子节点追加至队列中等待处理
        queue = [self.root]
        while queue:
            # 弹出第一个节点, 进行处理
            curr_node = queue.pop(0)
            # 若该节点有子节点, 则将子节点追加至队列末尾, 若无子节点, 则将新节点接入该节点下面
            if curr_node.left_child is not None:
                queue.append(curr_node.left_child)
            else:
                curr_node.left_child = node
                return
            if curr_node.right_child is not None:
                queue.append(curr_node.right_child)
            else:
                curr_node.right_child = node
                return

    def breadth_travel(self):
        """广度优先搜索"""
        if self.root is None:
            print(None)
            return
        queue = [self.root]
        print(self.root.data, end=" ")
        while queue:
            curr_node = queue.pop(0)
            left_child = curr_node.left_child
            if left_child:
                print(left_child.data, end=" ")
                queue.append(left_child)
            right_child = curr_node.right_child
            if right_child:
                print(right_child.data, end=" ")
                queue.append(right_child)

#               0
#         1           2
#     3       4   5       6
# 7       8
# 先序, 中序, 后序都是针对根节点来说或者父节点来说的
# 先序: 即0为第一个, 顺序为0-1-2
# 中序: 即0为第二个, 顺序为1-0-2
# 后序: 即0为第三个, 顺序为1-2-0

    def preoder(self, node):
        """先序遍历"""
        if node is None:
            return
        print(node.data, end=" ")
        self.preoder(node.left_child)
        self.preoder(node.right_child)

#               0
#         1           2
#     3       4   5       6
# 7       8
# 先序, 中序, 后序都是针对根节点来说或者父节点来说的
# 先序: 即0为第一个, 顺序为0-1-2
# 中序: 即0为第二个, 顺序为1-0-2
# 后序: 即0为第三个, 顺序为1-2-0

    def inoder(self, node):
        """中序遍历"""
        if node is None:
            return
        self.inoder(node.left_child)
        print(node.data, end=" ")
        self.inoder(node.right_child)

#               0
#         1           2
#     3       4   5       6
# 7       8
# 先序, 中序, 后序都是针对根节点来说或者父节点来说的
# 先序: 即0为第一个, 顺序为0-1-2
# 中序: 即0为第二个, 顺序为1-0-2
# 后序: 即0为第三个, 顺序为1-2-0

    def postoder(self, node):
        """后序遍历"""
        if node is None:
            return
        self.postoder(node.left_child)
        self.postoder(node.right_child)
        print(node.data, end=" ")


if __name__ == '__main__':
    binary_tree = BinaryTree()
    binary_tree.add(0)
    binary_tree.add(1)
    binary_tree.add(2)
    binary_tree.add(3)
    binary_tree.add(4)
    binary_tree.add(5)
    binary_tree.add(6)
    binary_tree.add(7)
    binary_tree.add(8)
    print("广度优先遍历")
    binary_tree.breadth_travel()
    print("")
    print("深度先序遍历")
    binary_tree.preoder(binary_tree.root)
    print("")
    print("深度中序遍历")
    binary_tree.inoder(binary_tree.root)
    print("")
    print("深度后序遍历")
    binary_tree.postoder(binary_tree.root)
