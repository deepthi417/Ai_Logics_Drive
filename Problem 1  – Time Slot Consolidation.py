n = int(input())
ranges = []
for _ in range(n):
    start, end = map(int, input().split())
    ranges.append([start, end])
# Sorting  ranges by starting time
ranges.sort()
merged = []

for start, end in ranges:
    if not merged:
        merged.append([start, end])
    else:
        last_start, last_end = merged[-1]
        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])
# Printing ranges
for start, end in merged:
    print(start, end)
