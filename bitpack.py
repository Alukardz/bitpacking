import math
import sys
import os
from char_char import read_char, read_int


doc_dir = os.path.join(os.getcwd(), sys.argv[1])

def main():
    ced = '03104263227'
    name = 'Vlad'
    lastname = 'Delar'
    packed_info = 0
    age = 200
    sex = 'M'
    civil_state = 'C'
    grade = 'P'


    packed_info = age << 4

    if sex == 'M':
        packed_info = packed_info | 8

    if civil_state == 'C':
        packed_info = packed_info | 4

    if grade == 'P':
        packed_info = packed_info | 3

    elif grade == 'G':
        packed_info = packed_info | 2

    elif grade == 'B':
        packed_info = packed_info | 1

    print(f'{packed_info:b}')
    print(packed_info)



if len(sys.argv) >= 2:
    main()
else:
    print('Especificar document. ej. reg_data.py datos.csv')