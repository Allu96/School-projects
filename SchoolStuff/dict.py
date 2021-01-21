def dictionary(n):
    if n < 0:
        print("negatiivinen syöte")
        exit()
    else:
        dict = {}
        for i in range(1,n+1):
            dict[i] = i*i

        return dict

def main():
    print("Syota kokonaisluku:")
    n = int(input())
    print(dictionary(n))

main()