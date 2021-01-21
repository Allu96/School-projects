import math

def main():
    r = int(input("Enter an positive integer:"))
    if r < 0:
        print("Negative number!")
        return -1
    else:
        print(int((math.sqrt(2)*r)*(math.sqrt(2)*r)))
main()