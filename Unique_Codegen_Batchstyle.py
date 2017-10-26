# Generation of 6 alphanum characters gives 1.838 billion possible unique characters
# You could also generate ~60 million unique characters using numeric

from numpy import random
from datetime import *
import shelve
import os.path


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
                # 10 = a, but we want A, which is 65
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


def save_data(codelist):
    shelf_file = shelve.open('codelist_data')
    shelf_file['codelist'] = codelist


def load_data():
    shelf_file = shelve.open('codelist_data')

    return shelf_file['code_list']


def main():
    num_characters = eval(input("Enter number of characters: "))
    num_codes = eval(input("Enter number of codes to generate: "))
    batch_signature = str(input("Enter batch code, eg. *B*5**: "))
    csv_header = str(input("Enter column heading for csv: "))

    start_time = datetime.now()
    try:
        codelist = load_data()
    except KeyError:
        print('No previous data. Creating New List.')
        codelist = []

    if os.path.exists('code_list.csv'):
        file = open('code_list.csv', 'w')
        file.write(csv_header)
        file.write('\n')
        file.close()

    for i in range(num_codes):
        new_code = generate_codestring(num_characters, read_batch_signature(batch_signature))
        if check_uniqueness(new_code, codelist):
            file = open('code_list.csv', 'a')
            file.write(new_code)
            file.write('\n')
            file.close()

            codelist.append(new_code)

    print("Done.")
    end_time = datetime.now()
    total_time = end_time - start_time
    print("Compute Time: ", total_time)
    save_data(codelist)


if __name__ == '__main__':
    main()