n = int(input())
k = int(input())

matrix = [[input() for j in range(k)] for i in range(n)]

for i in range(n):
    for j in range(k):
        print(matrix[i] [j], end='\t')
    print()
