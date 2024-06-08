
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


def function(valueA, valueB, *values):
    pass
function(1, 2, 3, 4, 5,)


# 56강

a = [1, 2, 3, 4]
b = a

a = [5, 6, 7, 8]
a.append(5)

print(a)
print(b)


a = 10
b = [1, 2, 3, 4]

print(a, b)

def function_a(c,d):
    c = 20
    d = [5, 6, 7, 8]
function_a(a,b) 
print(a, b)   

def function_b(c,d):
    c = 30
    d.extend([9, 10])
function_b(a,b)    
print(a,b) 



# 57강

# 재귀함수 - 자기자신을 호출하는 함수 - 팩토리얼 연산
# n! = n * (n-1) * (n-2) * .... * 1
# 3! = 3 * 2 *1
# - 반복문으로 구현
def factorial(n):
    output = 1
    for i in range(1, n + 1):
        output *= i
    return output

print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))

# - 재귀함수로 구현 
# - 수학의 수열의 점화식
# - 팩토리얼 점화식
# - 1! = 1
# (n이 2 이상의 수일때) n! = n * (n-1)!

def factorial(n):
    # 1! = 1
    if n == 1:
        return 1
    #(n이 2 이상의 수일 때) n! = n * (n-1)!
    elif n >= 2:
        return n * factorial(n - 1)
    
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))


# 58강

# 피보나치 수열
# a_1 = 1
# a_2 = 1
# a_n = a_{n-1} + a_{n-2}
# a_3 = 1 + 1 = 2
# a_4 = a_3 + a_2 = 2 + 1 = 3
# a_5 = a_4 + a_3 = 3 + 2 = 5
# .....
memo = {}
def f(n):
    # a_1 = 1
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    # a_2 = 1
    elif n == 2:
        return 1
    # a_n = a_{n-1} + a_{n-2}
    else:
        temp = f(n - 1) + f(n - 2)
        memo[n] = temp
        return temp

print(f(50))
print(memo)



memo = {1: 1, 2: 1}
def f(n):
    # a_1 = 1
    if n in memo:
        return memo[n]
    
    else:
        temp = f(n - 1) + f(n - 2)
        memo[n] = temp
        return temp

print(f(50))
print(memo)

# 바다사자 연산자 최근 파이썬


def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output.extend(flatten(item))
        else:    
            output.append(item)
    return output

data = [[1,2,3], [4,[5, 6]], 7, [8,9]]    
print(flatten(data))


a = (1,2,3)
b = (1,)

print(b)


A = ["바나나", "사과", "고구마", "감자"]

for i,item in enumerate(A):
    print(i, item)

B = {
    "이름": "별",
    "생일": (2019, 11, 14)
}

for key, value in B.items():
    print(key, value)


# 61강 콜백함수

def call_10_times():
    print("호출되었습니다!!")

a = call_10_times
print(a)

a()



def call_10_times(콜백함수):
    for i in range(10):
        콜백함수(i)

def print_hello(매개변수):
    print("안녕하세요!", 매개변수)
 

call_10_times(print_hello)



def power(숫자):
    return 숫자 ** 2

A = [1, 2, 3, 4, 5]
이터레이터 = map(power, A)
print(list(이터레이터))



# filter(함수, 리스트)
# 리스트의 요소를 함수에 전달했을 때
# 결과로 True가 나오는 녀석을 모아서
# 새로운 이터레이터를 만듦

def 홀수인가요(숫자):
    if 숫자 % 2 == 1:
        return True
    else:
        return False
A = [1, 2, 3, 4, 5]
이터레이터 = filter(홀수인가요, A)
print(list(이터레이터))


print([
    # 표현식
    숫자
    # 반복문
    for 숫자 in range(1, 5+1)
    # 조건문
    if 숫자 % 2 == 1
])

def my_map(콜백함수, 리스트):
    output = []
    for 요소 in 리스트:
        output.append(콜백함수(요소))
    return output

def power(숫자):
    return 숫자 ** 2
A = [1, 2, 3, 4, 5]
print(my_map(power, A))

# 62강

def my_filter(콜백함수,리스트):
    output = []
    for 요소 in 리스트:
        if 콜백함수(요소) == True:
            output.append(요소)
    return output

def is_odd(숫자):
    return 숫자 % 2 == 1

A = [1, 2, 3, 4, 5]
print(my_filter(is_odd, A))


# 63강
# 람다: 간단한 함수를 간단하게 해주는 문법
#def power(숫자):
#    return 숫자 ** 2

power = lambda 숫자: 숫자 ** 2
print(power(10))

#def is_odd(숫자):
#    return 숫자 % 2 == 1

is_odd = lambda 숫자: 숫자 % 2 == 1
print(power(10))

A = [1, 2, 3, 4, 5]

이터레이터 = map(lambda 숫자: 숫자 ** 2, A)
print(list(이터레이터))

이터레이터 = filter(lambda 숫자: 숫자 % 2 == 1, A)
print(list(이터레이터))



A = [52, 273, 32, 103, 57]
print(min(A))
print(max(A))

A = [{
    "제목": "혼자 공부하는 파이썬",
    "가격": 18000
}, {
    "제목": "혼자 공부하는 머신런닝 + 딥러닝",
    "가격": 26000
}, {
    "제목": "혼자 공부하는 자바스크립트",
    "가격": 24000
}]

print(min(A, key=lambda 책: 책["가격"] ))
print(max(A, key=lambda 책: 책["가격"] ))
A.sort(key=lambda 책: 책["가격"])
print(A)



# 64강
# 파일처리
# 읽기 처리/ 쓰기 처리

# (1) 스트림 연결(stream)
# w 쓰기모드, a 추가해서 쓰기 모드, r 읽기 모드 
파일 = open("test.txt", "r")
# (2) 스트림을 통해 데이터 통신
문자열 = 파일.read()
print(문자열)

# (3) 스트림 해제
파일.close()


 
with open("test.txt", "r") as 파일:
    문자열 = 파일.read()
    print(문자열)



with open("a.txt", "w") as 파일:
    파일.write("Hello World")

    

파일 = open("data1.txt", "r")
데이터 = 파일.read()
if 데이터 != "":
    print(데이터.strip().split("\n"))
파일.close()

문자열 = input("> 데이터를 입력해주세요: ")

파일 = open("data1.txt", "a")
파일.write(문자열 + "\n")
파일.close()

# 65강

import random
한글 = list("가나다라마바사아자차카타파하")

파일 = open("human.txt", "w")
파일.write("이름,몸무게,키\n")
print("이름,몸무게,키")
for i in range(1000):
    이름 = random.choice(한글) + random.choice(한글)
    몸무게 = random.randrange(40, 120)
    키 = random.randrange(140, 200)
    파일.write(f"{이름},{몸무게},{키}\n")
    # print(f"{이름},{몸무게},{키}")
    # print("{},{},{}".format(이름, 몸무게, 키))
    # print(",".join([이름, str(몸무게), str(키)]))
파일.close()


파일 = open("human.txt", "r")

for 한줄 in 파일:
    이름,몸무게,키 = 한줄.strip().split(",")

    if not 몸무게.isdigit():
        continue
    몸무게 = int(몸무게)
    키 = int(키)
    bmi = 몸무게 / (키 / 100) **2
    결과 = ""
    if 25 <= bmi:
        결과 = "과체중"
    elif 18.5 <= bmi:
        결과 = "정상체중"
    else:
        결과 = "저체중"
    # print(이름,몸무게,키,bmi,결과)
    # print(한줄.strip().split(","))
    print("\n".join([
        f"이름: {이름}",
        f"몸무게: {몸무게}",
        f"키: {키}",
        f"bmi: {bmi}",
        f"결과: {결과}", ""
    ]))

파일.close()    


# 66강
# 이터러블 : 반복할 수 있는것
# 이터레이터 : 반복하는 녀석
# 제너레이터 표현식
# 이터러블(반복문 뒤에 넣은 것)
# 이터레이터
# - 이터러블을 만드는 방법 중 하나
# - next(이터레이터): 내부의 요소를 꺼낼 수 있음
# 제너레이터
# - 이터레이터를 만드는 방법중 하나
범위 = range(1, 100 + 1)
리스트내포 = [
    i * i 
    for i in 범위
]
# print(리스트내포)

제너레이터표현식 = (
    i * i
    for i in 범위
)
for 요소 in 제너레이터표현식:
    # print(요소)
#print(next(제너레이터표현식))
#print(next(제너레이터표현식))
#print(next(제너레이터표현식))
# print(제너레이터표현식)
# 제너레이터 함수
제너레이터표현식 = (
    i * i
    for i in 범위
)



def 제너레이터함수():
    for i in range(1,100 + 1):
        yield i * i

제너레이터 = 제너레이터함수()
for 요소 in 제너레이터:
    print(요소)        
    

# 67강

파이 = 3.141592

# 유지보수

def 숫자입력():
    number_input_a = input(">  숫자 입력:")
    return float(number_input_a)

def 둘레구하기(radius):
    return 2 * 파이 * radius

def 넓이구하기(radius):
    return 파이 * radius * radius

반지름 = 숫자입력()
print(둘레구하기(반지름))
print(넓이구하기(반지름))



# 68강

전체사람수 = 6
카운터 = 0

def 그래프(노드, 이전화살표에적인숫자):
    if 노드 == 0:
        global 카운터
        카운터 += 1
    for i in range(max(2, 이전화살표에적인숫자), min(노드, 10) + 1):
        그래프(노드 - i, i)

그래프(전체사람수, 0)
print(카운터)


# 69강
# 깊이우선 탐색부

전체사람수 = 6
메모 = {}

def 그래프(노드, 이전화살표에적힌숫자):
    
    # 튜플: 이뮤터블 자료형 -> 딕셔너리의 키로 사용가능
    if (노드, 이전화살표에적힌숫자) in 메모:
       return 메모 [(노드, 이전화살표에적힌숫자)]
    
    # 일반적인 상황
    리턴값 = 0
    if 노드 == 0:
        리턴값 += 1
    else:
       for i in range(max(2, 이전화살표에적힌숫자), min(노드, 10) + 1):
        리턴값 += 그래프(노드 - i, i)
    메모 [(노드, 이전화살표에적힌숫자)] = 리턴값    
    return 리턴값    
import time
실행이전시간 = time.time()
print(그래프(전체사람수, 0))
실행이후시간 = time.time()
print(실행이후시간 - 실행이전시간)



# 70강 
# 하노이탑

카운터 = 0

def 하노이탑(원판개수, 시작기둥, 대상기둥, 보조기둥):
    global 카운터
    if 원판개수 == 1:
        # print(시작기둥, "->", 대상기둥)
        카운터 += 1
    else:
        하노이탑(원판개수 - 1, 시작기둥, 보조기둥, 대상기둥)
        # print(시작기둥, "->", 대상기둥)
        카운터 += 1
        하노이탑(원판개수 - 1, 보조기둥, 대상기둥, 시작기둥)

원판개수 = int(input("원판의 개수를 입력하세요: "))
하노이탑(원판개수, "A", "B", "C")
print(카운터)


원판개수 = int(input("원판의 개수를 입력하세요: "))
print((2**원판개수) - 1)

# 원판 1개 : 1 = 2 - 1
# 원판 2개 : 3 = 4 - 1
# 원판 3개 : 7 = 8 - 1 
# 원판 4개 : 15 = 16 - 1
# 원판 5개 : 31 = 32 - 15



#73강

입력 = input("정수입력> ")

if 입력.isdigit():
    숫자입력 = int(입력)
    print(f"원의 반지름: {숫자입력}")
    print(f"원의 둘레: {2 * 3.14 * 숫자입력}")
    print(f"원의 넓이: {3.14 * 숫자입력 * 숫자입력}")

else:
    print("정수를 입력하지 않았습니다.")


#74강

입력 = input("정수입력> ")

try:
    숫자입력 = int(입력)
    print(f"원의 반지름: {숫자입력}")
    print(f"원의 둘레: {2 * 3.14 * 숫자입력}")
    print(f"원의 넓이: {3.14 * 숫자입력 * 숫자입력}")
except:    
     print("정수를 입력하지 않았습니다.")

 
입력 = input("숫자입력> ")

try:
    숫자입력 = float(입력)
    print(f"원의 반지름: {숫자입력}")
    print(f"원의 둘레: {2 * 3.14 * 숫자입력}")
    print(f"원의 넓이: {3.14 * 숫자입력 * 숫자입력}")
except:    
     print("정수를 입력하지 않았습니다.")

try :
     예외가 발생할 가능성이 있는 코드

except:
     예외가 발생했을 때 실행할 코드

       

try :
     예외가 발생할 가능성이 있는 코드

except:



입력리스트 = ["52", "273", "32.1", "103", "숫자로변환할수없는 문자열"]
출력리스트 = []

for 요소 in 입력리스트:
    try:
        출력리스트.append(float(요소))
    except:
        pass

print(출력리스트)



def isfloat(입력):
    try:
        float(입력)
        return True
    except:
        return False
    
입력리스트 = ["52", "273", "32.1", "103", "숫자로변환할수없는 문자열"]
출력리스트 = []

for 요소 in 입력리스트:
    try:
        출력리스트.append(float(요소))
    except:
        pass

print(출력리스트)



# 75강

try :
     예외가 발생할 가능성이 있는 코드
     pass
except:
     예외가 발생했을 때 실 행할 코드
     pass
else:
     예외가 발생하지 않았을 때 실행할 코드
     pass
finally:
     무조건 생행하는 코드
     pass


def 함수(파일이름):

    try:
        파일 = open(파일이름, "r")
        내용 = 파일.read()
        try:
            숫자 = int(내용)
            return 내용
        except:
            print("숫자로 변환할 수 없는 파일입니다.")
        finally:
            파일.close()
    except:
        print("존재하지 않는 파일입니다.")

파일이름 = input("파일 이름> ")
print(함수(파일이름))



def 함수(파일이름):
    파일 = None
    try:
        파일 = open(파일이름, "r")
        내용 = 파일.read()
        숫자 = int(내용)
        return 내용
    except FileNotFoundError:
        print("존재하지 않는 파일입니다.")
    except ValueError:
        print("숫자로 변환할 수 없는 파일입니다.")
    finally:
        if 파일 != None:
            파일.close()
    
파일이름 = input("파일 이름> ")
print(함수(파일이름))


try:
    [사용자로부터 어떤 입력을 받고, 네트워크로 그걸 전송하는 프로그램]
except Exception as e:
    if type(e) == ValueError:
        print("값을 다시 제대로 입력해주세요.")
    elif type(e) ==ConnectionError:
        print("인터넷 연결에 문제가 있습니다.")
    else:
        i = input("오류 내용을 전송하시겠습니까? [Y/N]")
        if i in ["Y", "y"]:
            메일보내기(type(e), str(e))

try:
    dasdasd[0]
except Exception as e:
    print(type(e))
    print(e)
 
try:
    [사용자로부터 어떤 입력을 받고, 네트워크로 그걸 전송하는 프로그램]
except Exception as e:
    if type(e) == ValueError:
        print("값을 다시 제대로 입력해주세요.")
    elif type(e) == ConnectionError:
        print("인터넷 연결에 문제가 있습니다.")
    else:
        i = input("오류 내용을 전송하시겠습니까? [Y/N]")
        if i in ["Y","y"]:
            메일보내기(type(e), str(e))

try:
    int("asd")
except ValueError:
    print("값을 다시 제대로 입력해주세요.")
except ConnectionError:
    print("인터넷 연결에 문제가 있습니다.")
except Exception as e:    
    i = input("오류 내용을 전송하시겠습니까? [Y/N]")
    if i in ["Y", "y"]:
        메일보내기(type(e), str(e))

# 77강

number = input("정수 입력> ")
number = int(number)

if number > 0:
    print("양수입니다")
elif number == 0:
    raise Exception("아직 구현되지 않았습니다.")
else:
    raise Exception("아직 구현되지 않았습니다.")



def 사각형넓이구하기(너비,높이):
    if 너비<= 0 or 높이 <= 0:
        raise ValueError("너비와 높이는 양수여야합니다")
    return 너비 * 높이
print(사각형넓이구하기(0, -1))




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

# 문제(1) 합계를 구하는 함수가 있는지 + 평균을 구하는 함수가 있는지 자체를 모름
# 문제(2) "학생들"이라는 변수에 직접적으로 접근할 수 있다는것
# 문제(3) 함수가 분산되어 있다
# 그래서 class사용함

print("이름","총점","평균", sep="\t")

for 학생 in 학생들:
    총점 = sum_student(학생)
    평균 = average_student(학생)
    print(학생["이름"],총점, 평균, sep="\t" ) 



# 80강

class 학생:
    # 클래스의 내용

    def 초기화(self,이름,국어,영어,수학,과학):
        self.이름 = 이름
        self.국어 = 국어
        self.영어 = 영어
        self.수학 = 수학
        self.과학 = 과학
    def sum(self):
        return self.국어 + self.수학 + self.영어 + self.과학
    def average(self):
        return self.sum() / 4
# 객체(인스턴스)
인성 = 학생()
# 함수 호출방법(1)
학생.초기화(인성,"인성",87, 88, 98, 95)
print(인성.이름,인성.국어)


#함수 호출방법(2)

인성.초기화("인성",87, 88, 98, 95)
인성.sum()
인성.average()

print(인성.이름, 인성.국어)


class 학생:
    # 클래스의 내용
    
    def __init__(self,이름,국어,영어,수학,과학):
    def sum(self):
    def average(self):

# 객체(인스턴스)
학생들 = [
    학생("인성",87,88,98,95),
    학생("구름",92,98,97,98),
    학생("별이",76,96,95,90)
]

print("이름","총점","평균", sep="\t")

for 학생 in 학생들:
    총점 = sum_student(학생)
    평균 = average_student(학생)
    print(학생["이름"],총점, 평균, sep="\t" ) 

# 스네이크 케이스: create_student  -> 대부분
# 대문자 캐멜케이스: CreateStudent -> 클래스
class Student:
    # 클래스의 내용
    
    def __init__(self,이름,국어,영어,수학,과학):
    def sum(self):
    def average(self):
    def print(self):    

 
class StudentList :
    
    def__init__(self):
    def add(self, student):
    def print(self):

Student = StudentList()
Student.add(Student("인성",87, 88, 98, 95))
Student.add(Student("구름",92, 98, 97, 98))
Student.add(Student("별이",76, 96, 95, 90))
Student.print()

print("이름","총점","평균", sep="\t")

for 학생 in 학생들:
    총점 = sum_student(학생)
    평균 = average_student(학생)
    print(학생["이름"],총점, 평균, sep="\t" ) 

  

# 스파르타 클래스강좌

class Monster():
    hp = 100
    alive = True

    def damage(self, attack):
        self.hp = self.hp - attack
        if self.hp < 0:
            self.alive = False

    def status_check(self):
        if self.alive:
            print("살았다")
        else:
            print("죽었다")

m1 = Monster()
m1.damage(150)
m1.status_check()

m2 = Monster()
m2.damage(90)
m2.status_check()


인성 = 학생()
# 함수 호출방법(1)
학생.초기화(인성,"인성",87, 88, 98, 95)
print(인성.이름,인성.국어)


#함수 호출방법(2)

인성.초기화("인성",87, 88, 98, 95)
인성.sum()
인성.average()

print(인성.이름, 인성.국어)



인성.이름 = "인성"
인성.국어 = 87
인성.영어 = 88
인성.수학 = 98
인성.과학 = 95

print(인성.이름)
print(인성.국어)  x 


# 81강
# 추후재시청

# 82강
# 추후재시청

 
class Circle:
    def __init__(self,반지름):
        if 반지름 < 0:
            raise TypeError("반지름은 0 이상이어야 합니다.")
        self.__반지름 = 반지름
        self.__파이 = 3.14
    def get_반지름(self):
        return self.__반지름
    def set_반지름(self, value):
        if value < 0:
            raise TypeError("반지름은 0 이상이어야 합니다.")
        self.__반지름 = value        
    def 둘레(self):
        return 2 * self.__파이 * self.__반지름
    def 넓이(self):
        return self.__파이 * (self.__반지름 **2)
    
circle = Circle(10)
# circle.반지름 = -10
print(circle.get_반지름())
circle.set_반지름(20)
print(circle.둘레())
print(circle.넓이())



# 83강
 
파이 = 3.14
반지름 = 10
넓이 = 반지름 * 반지름 * 3.14

print("=" * 10)
print("*" * 10)
print("=" * 10)
print(f"원의 반지름: {반지름}")
print(f"넓이: {넓이}")
print("=" * 10)
print("*" * 10)
print("=" * 10)


class Circle:
    def __init__(self, 반지름):
        self.파이 = 3.14
        self.반지름 = 반지름
    def 넓이(self):
        return self.반지름 * self.반지름 * self.파이
    
    def 출력(self):
        print("=" * 10)
        print("*" * 10)
        print("=" * 10)
        print(f"원의 반지름: {self.반지름}")
        print(f"넓이: {self.넓이()}")
        print("=" * 10)
        print("*" * 10)
        print("=" * 10)

class Sqaure:
    def __init__(self, 길이):
        self.길이 = 길이
    def 넓이(self):
        return self.길이 ** 2
    def 출력(self):
        print("=" * 10)
        print("*" * 10)
        print("=" * 10)
        print(f"정사각형 한 변의 길이: {self.길이}")
        print(f"넓이: {self.넓이()}")
        print("=" * 10)
        print("*" * 10)
        print("=" * 10)


circle = Circle(10)
circle.출력()

square = Sqaure(10)
square.출력()

 
class Shape:
    def __init__(self):
        raise "생성자를 구현해주세요."
    def 넓이(self):
        raise "넓이 함수를 구현해주세요. 넓이를 리턴하는 함수를 작성해주세요."
    def 출력보조(self):
        raise "출력보조 함수를 구현해주세요. 출력 전 한마디르 입력해주세요."
    def 출력(self):
        print("=" * 10)
        print("*" * 10)
        print("=" * 10)
        self.출력보조()
        print(f"넓이: {self.넓이()}")
        print("=" * 10)
        print("*" * 10)
        print("=" * 10)

class Circle(Shape):
    def __init__(self, 반지름):
        self.파이 = 3.14
        self.반지름 = 반지름
    def 출력보조(self):
        print(f"원의 반지름: {self.반지름}")
    def 넓이(self):
        return self.반지름 * self.반지름 * self.파이
    
class Square(Shape):
    def __init__(self, 길이):
        self.길이 = 길이
    def 출력보조(self):
        print(f"정사각형 한 변의 길이는: {self.길이}")
    def 넓이(self):
        return self.길이 ** 2

circle = Circle(10)
circle.출력()

square = Square(10)
square.출력()








# GPT 코드

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def circumference(self):
        return 2 * math.pi * self.radius

# 사용 예제
circle = Circle(5)
print("원의 둘레:", circle.circumference())



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

'''
# 85강
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
# 컴포지션 : 프레임워크가 강제하는 것이 없다면 

class Student:
    def __init__(self,수학):
        self.__리스트 = []
class StudentList(list):
    def __init__(self):
        self.__리스트 = []
    def append(self, 요소):
        if type(요소) != Student:
            raise "Student를 전달해주세요."
        self.__리스트.append(요소)
    def sum(self):
        output = 0
        for 학생 in self.__리스트:
            output += 학생.수학
        return output
    def average(self):
        return self.sum() / len(self.__리스트) 

학생목록 = StudentList()
학생목록.append(Student(100))
학생목록.append(Student(20))
print(학생목록.sum())
print(학생목록.average())  

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

# 실행안됨 휴~~~


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
'''
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





