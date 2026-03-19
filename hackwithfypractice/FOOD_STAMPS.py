import heapq

n = int(input("Enter n"))
m = int(input("Enter m"))

v = []
d = []

for _ in range(n):
    v.append(int(input()))

for _ in range(n):
    d.append(int(input()))

heap = []


for i in range(n):
    heapq.heappush(heap, (-v[i], i))
    
answer = 0

while m > 0 and heap:
    value, i = heapq.heappop(heap)

    value = -value  

    if value <= 0:
        break

    answer += value

    next_value = value - d[i]

    if next_value > 0:
        heapq.heappush(heap, (-next_value, i))

    m -= 1

print(answer)
#read the last page of your book to understand the logic