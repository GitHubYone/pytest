#リスト : 二分木 バイナリツリー
from icecream import ic
# 節
class Node:
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

#
# 操作関数
#

# 探索
def search(node, x):
    while node is not None:
        if node.item == x: return True
        elif x < node.item: node = node.left
        else: node = node.right
    return False

def search_min(node):
    while node.left is not None: node = node.left
    return node.item

def search_max(node):
    while node.right is not None: node = node.right
    return node.item

# 挿入
def insert(node, x):
    if node is None:
        return Node(x)
    elif x < node.item:
        node.left = insert(node.left, x)
    elif x > node.item:
        node.right = insert(node.right, x)
    return node

# 削除
def delete_min(node):
    if node.left is None: return node.right
    node.left = delete_min(node.left)
    return node

def delete_max(node):
    if node.right is None: return node.left
    node.right = delete_max(node.right)
    return node

def delete(node, x):
    if node is None: return node
    if node.item == x:
        if node.left is None: return node.right
        if node.right is None: return node.left
        node.item = search_min(node.right)
        node.right = delete_min(node.right)
    elif x < node.item:
        node.left = delete(node.left, x)
    else:
        node.right = delete(node.right, x)
    return node

# 巡回
def each(node):
    if node is not None:
        yield from each(node.left)
        yield node.item
        yield from each(node.right)

# 二分木
class Tree:
    def __init__(self):
        self.root = None

    # 挿入
    def insert(self, x):
        self.root = insert(self.root, x)

    # 探索
    def search(self, x):
        return search(self.root, x)

    def max(self):
        if self.root is None: return None
        return search_max(self.root)

    def min(self):
        if self.root is None: return None
        return search_min(self.root)

    # 削除
    def delete(self, x):
        self.root = delete(self.root, x)

    def delete_max(self):
        if self.root is not None: delete_max(self.root)

    def delete_min(self):
        if self.root is not None: delete_min(self.root)

    # 巡回
    def each(self): return each(self.root)

    # 空か？
    def is_empty(self): return self.root is None

    # 表示
    def __repr__(self):
        if self.root is None: return 'Tree()'
        s = 'Tree('
        for x in each(self.root):
            s += '{}, '.format(x)
        s = s[:-2]
        s += ')'
        return s

# テスト
if __name__ == '__main__':
    import random
    tree = Tree()
    data = [random.randint(0, 100) for x in range(10)]
    ic([random.randint(0, 100) for x in range(10)])
    print(data)
    print(tree)
    print(tree.is_empty())
    for x in data: tree.insert(x)
    print(tree)
    print(tree.is_empty())
    print('max =', tree.max())
    print('min =', tree.min())
    print("delete max")
    tree.delete_max()
    print(tree)
    print("delete min")
    tree.delete_min()
    print(tree)
    for x in data:
        print('search', x, tree.search(x))
        print('delete', x)
        tree.delete(x)
        print('search', x, tree.search(x))
        print(tree)