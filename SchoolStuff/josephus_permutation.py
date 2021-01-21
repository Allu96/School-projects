def who_goes_free(n, k):
    arr = [i for i in range(n)]
    m = k - 1 # laskuri, milloin alustetaan alkio viivaksi
    a = 0     # viivojen laskuri
    while a != (len(arr) - 1):
        for j in range(len(arr)):
            if m == 0:
                if arr[j] != "-":
                    arr[j] = '-'
                    a += 1
                    m = k - 1
                else:
                    continue
            else:
                if arr[j] == '-':
                    continue
                else:
                    m -= 1
    return [i for i in arr if i != "-"]

def main():
    n = int(input("Number of prisoners:"))
    k = int(input("Step size:"))
    print("Survivor:",who_goes_free(n, k))
main()