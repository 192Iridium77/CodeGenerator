from numpy import random
from datetime import *

def generate_codestring(code_length):
    codestring = ''
    i = 0
    while i < code_length:
        alphanum_select = random.randint(0, 36)
        if alphanum_select <= 9:
            codestring += str(alphanum_select)
        else:
            # 10 = a, but we want A, which is 65, therefore add 55
            codestring += chr(alphanum_select + 55)
        i += 1

    return codestring


def check_uniqueness(code, lst):
    if code in lst:
        return False
    return True


def main():
    codelist = []
    num_characters = eval(input("Enter number of characters: "))
    num_codes = eval(input("Enter number of codes to generate: "))
    start_time = datetime.now()
    for i in range(num_codes):
        new_code = generate_codestring(num_characters)
        if check_uniqueness(new_code, codelist):
            codelist.append(new_code)
    print("Done.")
    end_time = datetime.now()
    total_time = end_time - start_time
    print("Compute Time: ", total_time)


if __name__ == '__main__':
    main()