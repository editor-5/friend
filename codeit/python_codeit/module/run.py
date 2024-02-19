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


print('run 파일 이름: {}'.format(__name__))

import area

print('run파일 실행됨')

# __name__
# __main__



import area

# 면적 계산기 프로그램
def main():
    x = float(input('원의 지름을 입력해 주세요: '))
    print('지름이 {}인 원의 면적은 {}입니다.\n'.format(x, area.circle(x)))

    y = float(input('정사각형의 변의 길이를 입력해 주세요: '))
    print('변의 길이가 {}인 정사각형의 면적은 {}입니다.'.format(y, area.square(y)))

if __name__ == '__main__':
    main()

   

import shapes.volume

print(shapes.volume.cube(3))



import shapes.volume as vol

print(vol.cube(3))



from shapes.area import square

print(square(3))



from shapes import volume
# import shapes.volume



import shapes

print(shapes.area.circle(2))



import shapes 

print(shapes.area.square(2))
print(shapes.volume.cube(2))



import shapes 

print(shapes.circle(2))
print(shapes.square(2))



import shapes 

shapes.PI

from shapes import PI
shapes.PI



from shapes import *

print(dir())



from mymath.stats.average import data_mean
from mymath.stats import average
import mymath.stats.average



from mymath import stats
import mymath.stats

from mymath import shapes
import mymath.shapes

'''








