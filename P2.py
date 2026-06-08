n = int(input())
arr = list(map(int, input().split()))
k = int(input())

window_sum = sum(arr[:k])
max_sum = window_sum

for i in range(k, n):
    window_sum += arr[i] - arr[i - k]
    max_sum = max(max_sum, window_sum)

print(max_sum)
