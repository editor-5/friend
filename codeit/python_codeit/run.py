'''
from area import circle, square
# import area as ar
# from import square as sq

print(circle(2))
print(square(2))

import area as ar

# print(dir(area))
print(dir())



from area import circle, square

print(dir())



from area import circle, square as sq

def square(length):
    return 4 * length

print(dir())
print(square(3))
print(sq(3))



import area

def square(length):
    return 4 * length

print(dir())
print(square(3))
print(area.square(3))



import math

math.log10()
math.cos() 

from math import log10, cos

log10()
cos() 



import sys

print(sys.path)


# 경로추가
import sys
 
sys.path.append('C:\\Users\\codeit\\Desktop') # Windows



import area

x = float(input('원의 반지름을 입력해 주세요: '))
print('반지름이{}인 원의 면적은 {}입니다.\n'.format(x, area.circle(x)))

'''
print('run 파일 이름: {}'.format(__name__))

import area

print('run파일 실행됨')

# __name__
# __main__