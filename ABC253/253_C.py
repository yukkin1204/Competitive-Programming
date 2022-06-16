# Max - Min Query
import heapq
from sys import exit

class HeapDict:
    def __init__(self):
        self.h1 = []
        self.h2 = []
        self.d = dict()

    def insert(self,x):
        heapq.heappush(self.h1,x)
        heapq.heappush(self.h2,-x)
        if x not in self.d:
            self.d[x] = 1
        else:
            self.d[x] += 1

    def erase(self,x):
        if x not in self.d or self.d[x] == 0:
            print(x,"is not in HeapDict")
            exit()
        else:
            self.d[x] -= 1

        while len(self.h1) != 0:
            if self.d[self.h1[0]] == 0:
                heapq.heappop(self.h1)
            else:
                break

        while len(self.h2) != 0:
            if self.d[-self.h2[0]] == 0:
                heapq.heappop(self.h2)
            else:
                break

    def is_exist(self,x):
        if x in self.d and self.d[x] != 0:
            return True
        else:
            return False

    def get_min(self):
        return self.h1[0]

    def get_max(self):
        return -self.h2[0]

Q = int(input())
hd = HeapDict()

for _ in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        hd.insert(query[1])
    elif query[0] == 2:
        while (query[2] > 0 and hd.is_exist(query[1])):
            hd.erase(query[1])
            query[2] -= 1
    else:
        print(hd.get_max() - hd.get_min())