n = int(input())
a = list(map(int, input().split()))
k = int(input())

left = 0
best = 0
start = 1
for right in range(n):
    while max(a[left:right+1]) - min(a[left:right+1]) > k:
        left += 1
    length = right - left + 1
    if length > best:
        best = length
        start = left + 1
print(best, start)
