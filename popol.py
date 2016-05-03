import random

def paramSweep(n, m):
    """Sweep n parameters in the range of [0,m]"""
    stack = [0]
    while stack:
        top = stack.pop()
        if top < m:
            stack.append(top + 1)
            if len(stack) == n:
                yield stack
            else:
                stack.append(0)

def objectsInBins(n, m, allowZero=False):
    """Put m objects in n bins"""
    n = n - 1
    arrange = [-1]
    while True:
        if len(arrange) == n:
            arrange.append(m - sum(arrange))
            if not allowZero:
                # check if zero exists
                hasZero = False
                for x in arrange:
                    if x == 0:
                        hasZero = True
                        break
                if not hasZero:
                    yield arrange
            else:
                yield arrange
        while arrange[-1] == m - sum(arrange[:-1]):
            arrange.pop()
            if len(arrange) == 0:
                return
        arrange[-1] += 1
        arrange += [0] * (n-len(arrange))


def dictEqual(a, b):
    """Compare if two dictionaries are equal"""
    return ordered(a) == ordered(b)

def ordered(obj):
    """Recursively sort an object by its keys"""
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k,v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj

class Heap(object):
    """A heap implementation that is more flexible than heapq"""
    def __init__(self, comp=lambda x, y: x < y):
        self.compare = comp
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def __nonzero__(self):
        return len(self.heap)

    def __str__(self):
        return str(self.heap)

    def insert(self, x):
        self.heap.append(x)
        a = self.heap
        i = len(self.heap) - 1
        parent = (i - 1) / 2
        while i > 0 and not self.compare(a[parent], a[i]):
            a[parent], a[i] = a[i], a[parent]
            i = parent
            parent = (i - 1) / 2

    def pop(self):
        ret = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify(0)
        return ret

    def peek(self):
        return self.heap[0]

    def heapify(self, a):
        self.heap = a
        for i in xrange(len(a)/2, -1, -1):
            self._heapify(i)

    def _heapify(self, i):
        a = self.heap
        size = len(a)
        left = 2 * i + 1
        right = 2 * i + 2

        j = None
        if left < size and not self.compare(a[i], a[left]):
            j = left
        if right < size and not self.compare(a[i], a[right]):
            if not (left < size and self.compare(a[left], a[right])):
                j = right

        if j is not None:
            a[i], a[j] = a[j], a[i]
            self._heapify(j)

class ListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.size = 0
        self.phead = ListNode(None)

    def __len__(self):
        return self.size

    def __getnode(self, idx):
        k = 0
        p = self.phead
        while k < idx:
            p = p.next
            k += 1
        return p

    def insert(self, idx, data):
        p = self.__getnode(idx-1)
        q = ListNode(data)
        q.next = p.next
        p.next = q
        self.size += 1

    def remove(self, idx):
        p = self.__getnode(idx-1)
        p.next = p.next.next
        self.size -= 1

    def __getitem__(self, idx):
        return self.__getnode(idx).data

class SkipNode(object):
    def __self__(self, data):
        self.data = data
        self.level = 1
        self.next = []
        self.width = []


class SkilList(object):
    def __init__(self):
        self.size = 0
        self.maxlevel = 1
        self.phead = SkipNode(None)

    def __len__(self):
        return self.size

    def __getnode(self, idx):
        cidx = 0
        p = self.phead
        while cidx < idx:
            for level in xrange(len(p.level), -1, -1):
                steps = p.width[level]
                if cidx + steps <= idx:
                    cidx = idx
                    p = p.next[level]
                    break
        return p

    def insert(self, idx, data):
        pass

    def remove(self, idx):
        pass

    def __getitem__(self, idx):
        return self.__getnode(idx).data

if __name__ == '__main__':
    h = Heap(lambda x, y: x > y)
    h.heapify([1,6,2,3,4,8,5,9])
    print h
