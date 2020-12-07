import math

packed_info = 0
age = 200
sex = 'M'
civil_state = 'C'
grado_academico = 'P'


packed_info = age << 4

if sex == 'M':
    packed_info = packed_info | 8

if civil_state == 'C':
    packed_info = packed_info | 4

if grado_academico == 'P':
    packed_info = packed_info | 3

elif grado_academico == 'G':
    packed_info = packed_info | 2

elif grado_academico == 'B':
    packed_info = packed_info | 1

print(f'{packed_info:b}')
print(packed_info)
