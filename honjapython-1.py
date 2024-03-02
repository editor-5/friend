
'''
# 7강

print("안녕\n하세요")
print("안녕\t하세\t요")
print("\\ \\ \\ \\")


# 39강
# while 반복문
a = [1, 2, 1, 2]
value = 2

while value in a:
    a.remove(value)
print(a)

# 1970년 1월 1일 0시 0분 0초
import time

시작시간 = time.time()
현재시간 = time.time()

while 현재시간 < 시작시간 + 5:
    print(현재시간, 시작시간 + 5) 
    현재시간 = time.time() 

# 40강
i = 0

while True:
    print(f"{i}번째 반복입니다")
    i += 1

    a = input("> 종료하시겠습니까?(y/n): ")
    if a in ["y", "Y"]:
        print("반복문을 종료합니다. ") 
        break  

numbers = [5, 15, 6, 20, 7, 25]

for i in numbers:
    if i >= 10:
        print(i)
    if i < 10:
        continue
    print(i)  

a= list(range(3, 10, 3))
print(a) 

# 42강 

a = [52, 273, 32, 103, 57]

print(max(a))
print(min(a))

print(max(52, 273, 32, 103, 57))
print(min(52, 273, 32, 103, 57))

print(sum(a))

for i in reversed(range(0, 10)):
    print(i)

a = range(0, 10)

for i in reversed(a):
    print(i)

fruits = ["바나나", "사과", "포도"]

i = 0
for fruit in fruits:
    print(f"{i}: {fruit}")

# enumerate() 함수
fruits = ["바나나", "사과", "포도"]
a = enumerate(fruits)
print(list(a))

for fruit in enumerate(fruits):
    print(fruit[0], fruit[1])

for i, fruit in enumerate(fruits):
    print(i,fruit)

# items() 함수
a = {
    "이름": "바나나",
    "가격": 1500,
    "원산지": "말레이시아"
}

for 키, 값 in a.items():
    # print(key, a[key])
    print(키, 값)
# 함수형 프로그래밍 이념 - reversed(a) , 객체 지향 프로그래밍 이념 - a.items() 

# 43강
# 리스트 내포 (List comprehension)
# 반복가능한 것을 기반으로
# 새로운 리스트를 만들어내는 문법
# An = 2n + 1(0 <= n < 10)
# A = {1, 3, 5, 7, 9, ..., 19}

A = []
for i in range(0, 10):
    A.append(2 * i + 1)
print(A)

달러 = [155.43, 302.71, 77.46, 131.28]
원화 = []
for dollal in 달러:
    원화.append(dollal * 1399)
print(원화) 

A = [2 * i + 1          # 표현식
    for i in range(0, 10)       # 반복문
    if i % 2 ==0        # 조건문
] 
print(A) 

달러 = [155.43, 302.71, 77.46, 131.28]
원화 = [dollal * 1399 for dollal in 달러]
print(원화)  

# 45강
number = int(input("정수 입력>"))

if number % 2 == 0:
    print("\n".join([
        f"입력한 문자열은{number}입니다.",
        f"{number}는(은) 짝수입니다."
    ]))
else:
    print("\n".join([
        f"입력한 문자열은{number}입니다.",
        f"{number}는(은) 홀수입니다."
    ])) 

print("\n".join([
    "A",
    "B",
    "C"
])) 

A=[ 
[3,2,4,5,10,20,30,40],
[1,2,2,6],
[-1,-2,2,4]
]
for a in A:
    a = [str(요소) for 요소 in a] 
    print(",".join(a)) 

# 45강

print(f"{10:b}")
print(f"{10:o}")
print(f"{10:x}")
print(int("1010", 2))
print(int("12", 8))
print(int("a", 16))  
a = []
for i in range(1 , 100 + 1):
    변환 = f"{i:b}"
    if 변환.count("0") == 1:
      print(i, ":", 변환)
      a.append(i)
print("합계:", sum(a)) 

a = [
    i    
    for i in range(1 , 100 + 1)    
    if f"{i:b}".count("0") == 1
]

for i in a:
    print(i, ":", f"{i:b}")
print("합계:", sum(a))  

# 46강

A = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]
카운터 = {}
for a in A:
    카운터[a] = 0

for a in A:
    카운터[a] += 1

print(카운터)
print(f"사용된 숫자의 종류는 {len(카운터)}개입니다.") 

A = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]

카운터 = {}
for a in A:
    if a not in 카운터:
        카운터[a] = 0
    카운터[a] += 1

print(카운터)
print(f"사용된 숫자의 종류는 {len(카운터)}개입니다.") 

A = "ctacaatgtcagtatacccattgcattagccgg"

카운터 = {}
for a in A:
    if a not in 카운터:
        카운터[a] = 0
    카운터[a] += 1

print(카운터)
print(f"사용된 숫자의 종류는 {len(카운터)}개입니다.")  

A = "ctacaatgtcagtatacccattgcattagccggaa"

카운터 = {}
for i in range(0, len(A), 3):
    a = A[i:i+3]
    if len(a) != 3:
        continue
    if a not in 카운터:
        카운터[a] = 0
    카운터[a] += 1

print(카운터)
print(f"사용된 숫자의 종류는 {len(카운터)}개입니다.")  

# 47강

A = [1, 2 ,[3, 4], 5, [6, 7], [8, 9]]
B = []

for a in A:
    if type(a) == list:
        print(a)
        for i in a:
            B.append(i)                
    else:
        B.append(a)

print(f"{A}를 평탄화하면")
print(f"{B}입니다") 



A = [1, 2 ,[3, 4], 5, [6, 7], [8, 9]]
B = []

for a in A:
    if type(a) == list:
        for i in a:
            B += [i]                
    else:
        B += [a]

print(f"{A}를 평탄화하면")
print(f"{B}입니다") 



# 50강

# 매개변수: 함수의 괄호 안에 넣는 변수
# parameter: 함수 정의 때 넣은 변수
def print_3_times(문자열,횟수):
    for i in range(횟수):
        print(문자열)
    
# argument: 함수 호출 때 넣은 값
print_3_times("안녕", 10)



# 51강

def print_n_times(횟수, *리스트):
    print(리스트)
    for i in range(횟수):
        for 요소 in 리스트:
            print(요소)
문자열목록 = ["안녕", "하세요"]
#print_n_times(2, "안녕", "하세요")
print_n_times(2, *문자열목록)



# 52강
print("안", "녕", "하", "세", "요",
      sep="::", end="")
print("안", "녕", "하", "세", "요",
      sep="::", end="")
print("안", "녕", "하", "세", "요",
      sep="::", end="")


def 함수(*가변, **딕셔너리):
    print(가변, 딕셔너리)

함수("안", "녕", "하",
   a=10, b=20, c=30)



# 53강

def f(x):
    return x + 1

print(f(1))
print(f(2))



def sum_all(start, end):

    output = 0
    for i in range(start, end +1):
        output += i
    return output

print(sum_all(1,10))
print(sum_all(1,100))
print(sum_all(1,1000))



# f(x) = 2x +1
def f(x):
    return 2 * x + 1

print(f(10))

# g(x) = x^2 + 2x + 1

def g(x):
    return x**2 + 2 * x + 1

print(g(10))



def mul(*values):
    output = 1
    for i in values:
        output *=i

    return output



print(mul(5, 7, 9, 10))
print(5*7*9*10)



def function(*values, valueA, valueB):
    pass
function(1, 2, 3, 4, 5, valueA=10, valueB=20)

'''
def function(valueA, valueB, *values):
    pass
function(1, 2, 3, 4, 5,)






'''# 77강
# raise Exception("예외를 강제로 발생시킵니다.")

number = input("정수 입력>")
number = int(number)

if number > 0:
    print("양수입니다")
elif number == 0:
    raise Exception("예외를 강제로 발생시킵니다.")
else:
    raise Exception("예외를 강제로 발생시킵니다.") 

def 사각형넓이구하기(너비,높이):
    if 너비 <= 0 or 높이 <=0:
        raise ValueError("너비와 높이는 양수여야합니다.")
    return 너비 * 높이

print(사각형넓이구하기(0,-1)) 

# 79강

def create_student(이름,국어,영어,수학,과학):
    return {"이름":이름,"국어":국어,"영어":영어,"수학":수학,"과학":과학}
def sum_student(학생):
    return 학생["국어"] + 학생["영어"] + 학생["수학"] + 학생["과학"]
def average_student(학생):
    return sum_student(학생) / 4
학생들 = [
    create_student("인성",87,88,98,95),
    create_student("구름",92,98,97,98),
    create_student("별이",76,96,95,90)
]


print("이름","총점","평균", sep="\t")

for 학생 in 학생들:
    총점 = sum_student(학생)
    평균 = average_student(학생)
    print(학생["이름"],총점, 평균, sep="\t" ) 

# 80강

class 학생:
    def 초기화(self,이름,국어,영어,수학,과학):
        self.이름 = 이름
        self.국어 = 국어
        self.영어 = 영어
        self.수학 = 수학
        self.과학 = 과학


인성 = 학생()

학생.초기화(인성,"인성",87, 88, 98, 95)

print(인성.이름,인성.국어)

인성.초기화("인성",87, 88, 98, 95)
print(인성.이름, 인성.국어)

인성.이름 = "인성"
인성.국어 = 87
인성.영어 = 88
인성.수학 = 98

인성.과학 = 95

print(인성.이름)
print(인성.국어)  x 

# 84강

class 부모:
    def 함수(self):
        print("부모의 함수입니다.")

class 자식(부모):
    def 함수(self):
        super().함수()
        print("자식의 함수입니다.")
        super().함수()

child = 자식()
child.함수()

class 빨간버튼:
    def __init__(self):
        print("버튼을 초기화합니다.")
        print("버튼을 만듭니다.")
        print("버튼을 화면에 출력합니다.")
        print("버튼을 빨간색으로 칠합니다.")

class 파란버튼:
    def __init__(self):
        print("버튼을 초기화합니다.")
        print("버튼을 만듭니다.")
        print("버튼을 화면에 출력합니다.")
        print("버튼을 파란색으로 칠합니다.")

class 초록버튼:
    def __init__(self):
        print("버튼을 초기화합니다.")
        print("버튼을 만듭니다.")
        print("버튼을 화면에 출력합니다.")
        print("버튼을 초록색으로 칠합니다.")  

빨간버튼()
파란버튼()
초록버튼()  

class 버튼:
    def __init__(self):
        print("버튼을 초기화합니다.")
        print("버튼을 만듭니다.")
        print("버튼을 화면에 출력합니다.")
        
class 빨간버튼:
    def __init__(self):
        super().__init__()
        print("버튼을 빨간색으로 칠합니다.")

class 파란버튼:
    def __init__(self):
        super().__init__()
        print("버튼을 파란색으로 칠합니다.")

class 초록버튼:
    def __init__(self):
        super().__init__()
        print("버튼을 초록색으로 칠합니다.")

빨간버튼()
파란버튼()
초록버튼()


class 버튼:
    def __init__(self, color):
        print(f"{color} 버튼을 초기화합니다.")
        print(f"{color} 버튼을 만듭니다.")
        print(f"{color} 버튼을 화면에 출력합니다.")
        
class 빨간버튼(버튼):
    def __init__(self):
        super().__init__("빨간색")
        print("빨간 버튼을 빨간색으로 칠합니다.")

class 파란버튼(버튼):
    def __init__(self):
        super().__init__("파란색")
        print("파란 버튼을 파란색으로 칠합니다.")

class 초록버튼(버튼):
    def __init__(self):
        super().__init__("초록색")
        print("초록 버튼을 초록색으로 칠합니다.")

빨간버튼()
파란버튼()
초록버튼()   

class Student:
    def __init__(self,수학):
        self.수학 = 수학
class StudentList(list):
    def append(self, 요소):
        if type(요소) != Student:
            raise "Student를 전달해주세요."
        super().append(요소)
    def sum(self):
        output = 0
        for 학생 in self:
            output += 학생.수학
        return output
    def average(self):
        return self.sum() / len(self) 

학생목록 = StudentList()
학생목록.append(Student(100))
학생목록.append(Student(20))
print(학생목록.sum())
print(학생목록.average())  

# 이코드는 현대사용안함 학생목록[0] = 0
# 상속과 컴포지션 상속: 프레임워크가 강제한다면 -> 상속
# 콤포지션 : 프레임워크가 강제하는 것이 없다면 

# 스택 선입후출
class Stack:
    def __init__(self):
        self.__List = []
    def push(self, value):
        self.__List.append(value)
    def pop(self):
        output = self.__List[-1]
        del self.__List[-1]
        return output
    
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.pop())
print(stack.pop())
print(stack.pop()) 

# 큐 선입선출

class Queue:
    def __init__(self):
        self.__List = []
    def enqueue(self, value):
        self.__List.append(value)
    def dequeue(self):
        output = self.__List[0]
        del self.__List[0]
        return output
    
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue()) 

# 87강
import math
print(math.sin(1))


import math as m
print(m.sin(1))

from math import sin, cos, tanh
print(sin(1))

import pandas as pd
import numpy as np
import tensorflow as tf

from bs4 import BeautifulSoup 

# 88강

from datetime import datetime

now = datetime.now()

print("현재 : ", now)
print("현재 날짜 : ", now.date())
print("현재 시간 : ", now.time())
print("timestamp : ", now.timestamp())
print("년 : ", now.year)
print("월 : ", now.month)
print("일 : ", now.day)
print("시 : ", now.hour)
print("분 : ", now.minute)
print("초 : ", now.second)
print("마이크로초 : ", now.microsecond)
print("요일 : ", now.weekday())
print("문자열 변환 : ", now.strftime('%Y-%m-%d %H:%M:%S'))

# Output
# 현재 :  2021-12-22 15:46:26.695840
# 현재 날짜 :  2021-12-22
# 현재 시간 :  15:46:26.695840
# timestamp :  1640155586.69584
# 년 :  2021
# 월 :  12
# 일 :  22
# 시 :  15
# 분 :  46
# 초 :  26
# 마이크로초 :  695840
# 요일 :  2
# 문자열 변환 :  2021-12-22 15:46:26

import random

print(random.uniform(10,20))
print(random.randrange(10,20))
print(random.choice([1,2,3,4,5,6]))

import sys

import os

import time

from urllib import request

target = request.urlopen("https://google.com")
print(target.read())  

# 89강

# (1) 프로그래밍 언어의 기본적인 문법
# (2-1) 알고리즘 문제 풀이
# 알고리즘 문제풀이
# 과거: 퀵소트를 구현해라, 머지소트를 구현해라
# 현대 : 미로를 탈출하는방법을 구해라, 최적의엘레베이터공식을 구해라등
# (2-2) 모듈공부
# 인공지능,데이터분석,웹개발

import os

output = os.listdir(".")
print("os.listdir():",output)
print()

print("# 폴더와 파일구분하기")
for path in output:
    if os.path.isdir(path):
        print("폴더:",path)
    else:
        print("파일:",path)

def read_folder(path):
    output = os.listdir(path)
    for item in output:
        if os.path.isdir(item):
            read_folder(path + "/" + item)
        else:
            print("파일: ", item)
read_folder(".")   '''
 

# 93강
# 웹서버개발 Django , Flask
# 인공지능개발 scikit-learn , tensorflow , keras
# 데이터분석 pandas , matplotlib 등이 모듈
# 크롤러 개발 Beautijul Soup , requests , scrapy 모듈
# 게임개발은 c# , c++ , 언니얼등





