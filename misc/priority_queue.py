# 「リストの要素の挿入」と「最小値（最大値）を取り出す」ことを繰り返すような時に使う
import heapq

a = [1, 5, 5, 0, -1]
heapq.heapify(a)

heapq.heappush(a, -99)  # add item
print(heapq.heappop(a))  # pop min

neg_a = [-x for x in a]
heapq.heapify(neg_a)
print(-heapq.heappop(neg_a))  # max
