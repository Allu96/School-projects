def letters(seq):
    upper = 0
    lower = 0
    for i in seq:
        if i.isupper():
            upper = upper + 1
        elif i.islower():
            lower = lower + 1
        else:
            continue

    return upper, lower

def main():
    s = input("Enter a sentence: \n")
    seq = list(s)
    print(letters(seq))
main()