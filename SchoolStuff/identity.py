def main():
    n = int(input())
    k = abs(n)
    arr = [[0 for i in range(k)] for j in range(k)]
    if n > 0:
        for i in range(n):
            for j in range(n):
                if i == j:
                    arr[i][j] = 1
    elif n == 0:
        print([])
    else:
        for j in range(abs(n)):
            k = abs(n)
            while k >= 0:
                if (j + k) == abs(n):
                    arr[j][k-1] = 1

                k -= 1

    for i in range(abs(n)):
        print(arr[i])

main()