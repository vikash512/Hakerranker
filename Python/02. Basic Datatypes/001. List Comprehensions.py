x, y, z, n = [int(input()) for _ in range(4)]
listOfAnswers = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
print(listOfAnswers)


or


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
list_ans= []
list_ans1 = []
for i in range (x+1):
    for j in range (y+1):
        for k in range (z+1):
            if (i+j+k)!=n:
              list_ans.append(i)
              list_ans.append(j)
              list_ans.append(k)
              list_ans1.append([i,j,k])
print(list_ans1)  
