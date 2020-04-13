n = int(input())
arr = list(map(int, input().split()))
zes = max(arr)
i=0
while(i<n):
    if zes ==max(arr):
        arr.remove(max(arr))
    i+=1
print(max(arr))


or

n = int(input())
arr = list(map(int, input().split()))
print(max([x for x in arr if x != max(arr)]))
