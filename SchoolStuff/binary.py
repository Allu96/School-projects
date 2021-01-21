def binary(b):
    div = []
    for i in b:
        bin = int(i,2)
        if (bin % 5 == 0):
            div.append(i)

    return div

def main():
    b = []
    numbers = str(input("Enter four binary numbers: "))
    splitted = numbers.split(",")
    for element in splitted:
        b.append(element)
    print(binary(b))

main()
