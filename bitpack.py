import math
import sys
from char_char import read_char, read_int


def main():
    ced = '03104263227'
    name = 'Vlad'
    lastname = 'Delar'
    packed_info = 0
    age = 200
    sex = 'M'
    civil_state = 'C'
    grade = 'P'
    data_list = [age, sex, civil_state, grade]
    packed_data = pack_data(data_list)
    final_data = f'{ced},{name},{lastname},{packed_data}'
    print(final_data)
    kp = unpack_data(packed_data)
    return final_data


def pack_data(data):
    packed_info = 0;
    age = data[0];
    sex = data[1];
    civil_state = data[2];
    grade = data[3];
    print(f'0-- {age:b}')

    packed_info = age << 4
    print(f'1-- {packed_info:b}')

    if sex == 'M':
        packed_info = packed_info | 8
        print(f'2-- {packed_info:b}')

    if civil_state == 'C':
        packed_info = packed_info | 4
        print(f'3-- {packed_info:b}')

    if grade == 'P':
        packed_info = packed_info | 3
        print(f'4-- {packed_info:b}')

    elif grade == 'G':
        packed_info = packed_info | 2
        print(f'5-- {packed_info:b}')

    elif grade == 'B':
        packed_info = packed_info | 1
        print(f'6-- {packed_info:b}')

    return packed_info


def unpack_data(packed_info):
    binary_data = 0
    count = 0
    while packed_info > 0:
        restante = packed_info % 2
        col = pow(10, count)
        binary_data += restante * col
        packed_info //= 2
        print(f'{count} {binary_data}')
        count += 1

    print(binary_data)
    return binary_data


def unpack_age(age):
    vdecimal = 0
    base1 = 1
    temp = age

    while temp > 0:
        ult_digit = temp % 10
        temp = temp / 10
        vdecimal += ult_digit * base1
        base1 = base1 * 2

    print(str(vdecimal))
    return str(vdecimal)


if len(sys.argv) >= 1:
    main()
else:
    print('Especificar document. ej. reg_data.py datos.csv')