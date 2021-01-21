def factorial(n):
    if n < 0:
        print("negatiivinen luku!")
    elif n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)

def main ():
    print("Syota kokonaisluku:")
    n = int(input())
    print("Kertoma on:")
    print(factorial(n))
main()


