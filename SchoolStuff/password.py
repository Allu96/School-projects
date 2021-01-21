def password(p_list):

    valid = []
    for p in p_list:
        if len(p) < 6 or len(p) > 12:
            continue
        lower, upper, number, spec_char = 0, 0, 0, 0
        for c in p:
            if c.islower():
                lower += 1
            elif c.isupper():
                upper += 1
            elif c.isnumeric():
                number += 1
            elif c == '#' or c == '@' or c == '$':
                spec_char += 1
        if lower > 0 and upper > 0 and number > 0 and spec_char > 0:
            valid.append(p)

    return valid

def main():

    P = []
    passwords = input("Enter passwords: ")
    splitted = passwords.split(",")
    for pword in splitted:
        P.append(pword)
    print(password(P))

main()