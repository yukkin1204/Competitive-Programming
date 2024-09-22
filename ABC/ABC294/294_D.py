from sys import stdin
import heapq

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

N, Q = map(int, input().split())
l = [list(map(int, stdin.readline().split())) for _ in range(Q)]

hd1 = HeapDict()
for i in range(N):
    hd1.insert(i + 1)
hd2 = HeapDict()

for event in l:
    if event[0] == 1:
        min = hd1.get_min()
        hd1.erase(min)
        hd2.insert(min)
    elif event[0] == 2:
        hd2.erase(event[1])
    else:
        print(hd2.get_min())
