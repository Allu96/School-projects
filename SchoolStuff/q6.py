import math

def calculator(D):
    C = 50
    H = 30
    result_list = []
    for i in range(0,len(D)):
        temp = round(math.sqrt((2*C*D[i])/H))
        result_list.append(temp)

    return result_list

def main():
    D = []
    n = int(input("Enter number of elements:"))
    num = str (input ("Enter comma separated integers: "))
    splitted = num.split(",")
    for element in splitted:
        D.append(int(element))
    print(calculator(D))

main()
