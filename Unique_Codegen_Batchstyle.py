# Generation of 6 alphanum characters gives 1.838 billion possible unique characters
# You could also generate ~60 million unique characters using numeric

from numpy import random
from datetime import *


def generate_codestring(code_length, batch_dict):
    codestring = ''
    i = 0
    while i < code_length:
        if i in batch_dict.keys():
            codestring += batch_dict[i]
            i += 1
        else:
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


# batch_sig is in format **C*8*, either numeric or uppercase alpha
def read_batch_signature(batch_sig):
    batch_dict = {}
    for i in range(len(batch_sig)):
        if batch_sig[i].isalpha():
            batch_dict[i] = batch_sig[i]
    return batch_dict


def main():
    codelist = []
    num_characters = eval(input("Enter number of characters: "))
    num_codes = eval(input("Enter number of codes to generate: "))
    batch_signature = str(input("Enter batch code, eg. *B*5**: "))
    start_time = datetime.now()
    for i in range(num_codes):
        new_code = generate_codestring(num_characters, read_batch_signature(batch_signature))
        if check_uniqueness(new_code, codelist):
            codelist.append(new_code)
    print("Done.")
    end_time = datetime.now()
    total_time = end_time - start_time
    print("Compute Time: ", total_time)


if __name__ == '__main__':
    main()