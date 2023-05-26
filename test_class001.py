#
# linkedlist.py : 連結リスト
#
#                 Copyright (C) 2018 Makoto Hiroi
#

# 連結リストクラス
from icecream import ic
class LinkedList:
    # セル
    class Cell:
        def __init__(self, data, link = None):
            self.data = data
            self.link = link

    # 連結リストの初期化
    def __init__(self, *args):
        self.top = LinkedList.Cell(None)   # ヘッダセル
        for x in reversed(args):
            self.insert(0, x)

    # n 番目のセルを求める
    def _nth(self, n):
        i = -1
        cp = self.top
        while cp is not None:
            if i == n: return cp
            i += 1
            cp = cp.link
        return None

    # 挿入
    def insert(self, n, x):
        cp = self._nth(n - 1)
        if cp is not None:
            cp.link = LinkedList.Cell(x, cp.link)
            return x
        return None

    # 参照
    def at(self, n):
        cp = self._nth(n)
        if cp is not None: return cp.data
        return None

    # 削除
    def delete(self, n):
        cp = self._nth(n - 1)
        if cp is not None and cp.link is not None:
            data = cp.link.data
            cp.link = cp.link.link
            return data
        return None

    # リストは空か
    def is_empty(self): return self.top.link is None

    # イテレータ
    def __iter__(self):
        self.index = self.top.link
        return self

    def __next__(self):
        if self.index is None:
            raise StopIteration
        data = self.index.data
        self.index = self.index.link
        return data

    # ジェネレータ
    def each(self):
        cp = self.top.link
        while cp is not None:
            yield cp.data
            cp = cp.link

    # リストの長さ
    def __len__(self):
        n = 0
        for _ in self.each(): n += 1
        return n

    # [] による参照
    def __getitem__(self, n):
        cp = self._nth(n)
        if cp is not None: return cp.data
        raise IndexError

    # [] による更新
    def __setitem__(self, n, x):
        cp = self._nth(n)
        if cp is not None:
            cp.data = x
            return None
        raise IndexError

    # del []
    def __delitem__(self, n):
        if self.delete(n) is None: raise IndexError

    # +
    def __add__(self, y):
        # リストのコピー
        def copy(a):
            if not a: return None
            return LinkedList.Cell(a.data, copy(a.link))
        # リストの連結
        def append(a, b):
            if a is None: return copy(b)
            return LinkedList.Cell(a.data, append(a.link, b))

        if not isinstance(y, LinkedList):
            raise NotImplementedError
        z = LinkedList()
        z.top.link = append(self.top.link, y.top.link)
        return z

    # 表示
    def __repr__(self):
        if self.top.link is None: return 'LinkedList()'
        s = 'LinkedList('
        for x in self.each(): s += '{}, '.format(x)
        return s[:-2] + ')'

    def __str__(self):
        return self.__repr__()

#
# 制限付き連結リスト
#
class FixedList(LinkedList):
    def __init__(self, limit, *args):
        self.limit = limit
        self.size = 0
        super().__init__(*args[:limit])

    # データの挿入
    def insert(self, n, x):
        if self.size < self.limit:
            result = super().insert(n, x)
            if result is not None: self.size += 1
            return result
        return None

    # データの削除
    def delete(self, n):
        if self.size > 0:
            result = super().delete(n)
            if result is not None: self.size -= 1
            return result
        return None

    # 表示
    def __repr__(self):
        if self.top.link is None: return 'FixedList({})'.format(self.limit)
        s = 'FixedList({}, '.format(self.limit)
        for x in self.each(): s += '{}, '.format(x)
        return s[:-2] + ')'

    def __str__(self):
        return self.__repr__()

# 簡単なテスト
if __name__ == '__main__':
    a = LinkedList()
    ic(a)
    ic(len(a))
    ic(a.is_empty())
    for x in range(5): a.insert(x, x)
    ic(a)
    print(len(a))
    print(a.is_empty())
    for x in range(5):
        print(a.at(x), a[x])
    for x in range(5):
        a[x] = a[x] * 10
    for x in a:
        print(x)
    for x in a.each():
        print(x)
    while not a.is_empty():
        # a.delete(0)
        del a[0]
    print(a)
    a = LinkedList(1,2,3,4,5)
    b = LinkedList(6,7,8,9,10)
    c = a + b
    print(a)
    print(b)
    print(c)
    c[0] = 10
    c[5] = 60
    print(a)
    print(b)
    print(c)

    # 制限付き連結リスト
    d = FixedList(5)
    print(d)
    for x in range(6):
        print(d.insert(0, x))
    print(d)
    while not d.is_empty():
        print(d.delete(0))
    print(d)