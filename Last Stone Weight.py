from heapq import *
from typing import List

class MaxHeap:
    def __init__(self, arr=[]):
        self.q = [-i for i in arr]
        heapify(self.q)

    def push(self, val):
        heappush(self.q, -val)

    def pop(self):
        return -heappop(self.q)

    def get_heap(self):
        return self.q

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        m = MaxHeap(stones)
        while len(m.get_heap()) > 1:
            stone = abs(m.pop() - m.pop())
            m.push(stone)
        return m.pop()

s = Solution()
print(s.lastStoneWeight([2,7,4,1,8,1]))