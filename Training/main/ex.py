a = input()
n = int(input())

if n < 1 or n > len(a):
    print('')
else:
    print(a[n - 1])
