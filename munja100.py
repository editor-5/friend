''' 
# 1번
print('maket "code" lab')
print("she's gone")
print('축하합니다. "우진"님!!') 

# 2번
a = 10
b = 20
print('a의 값은', a)
print('b의 값은', b)
print('a와 b의합은', a + b) 

# 8번
name = input("이름이 무엇인가요?")
age = int(input("몇 살인가요?"))

print( name, "님은 내년에는",age+1,"살이 됩니다.") 

# 9번 

a = int(input())
b = float(input())
c = a + b
d = c / 2

print('a와 b의 합은',c)
print('a와 b의 평균값은', d) 

# 10번

makit = 'Sieun Woojin!'
result = makit[0]

print(result)
result = makit[6]

print(result)
result = makit[12]

print(result) 


# 11번

makit = 'Sieun Woojin!'
result = makit[2:9]

print(result)
result = makit[:5]

print(result)
result = makit[6:]

print(result) 


# 12번

makit = '동서남북동서남북동서남북'
result = makit[::4]

print(result)
result = makit[2::4]

print(result) 


# 13번

makit = '동서남북'
result = makit[::-1]

print(result) 

# 14번

phone = '010-1234-5678'
new_phone = phone.replace('-','.')
print(new_phone)

name = 'makit code lab'
new_name = name.replace('a','A') 
print(new_name) 

# 17번

n = int(input('초를 입력하세요:'))
m = n
a = m//60 
m = m % 60
print(n,'초(sec)는',a,'분(min)',m,'초(sec)입니다') 

# 21번

a = ['우진','시은']
a.append('메이킷')
print(a)
del a[2]
print(a) 

# 22번

a = ['우진','시은','메이킷']
a.insert(1,'하워드')
print(a) 

# 23번

a = ['우진','시은']
b = ['메이킷','소피아','하워드']
a.extend(b)
print(a)
print(b) 

# 24번

a = ['우진','시은']
b = ['메이킷','소피아','하워드']
c = []
c.extend(a)
print(c)
c.extend(b)
print(c) 

# 25번

a = [3,7,4,5,6,8]
print('리스트 a의 개수 즉 길이는',len(a))
print('리스트 a의 숫자들의 평균은',sum(a)/len(a)) 

# 27번
a =['형우', '윤진', '시은', '유진']
b = a[-1:-5:-1]
print(b) 

# 29번

a = ['시은', '우진', '지훈', '지연']
b = ' '.join(a)
c = ','.join(a)
print(b)
print(c) 

# 30번

a = '신은 우진 지훈 지연'
b = a.split(' ')
print(b)  

# 31번

a,b,c = map(int, input().split())
print(min(a,b,c))  xx  

# 32번

x = int(input('첫 번째 점수를 입력하세요:'))
y = int(input('두 번째 점수를 입력하세요:'))

if x > y :
    print('makit')
else :
    print('woojin') 

# 33번

a = 3
b = 8
c = 17

if a% 2 == 1 :
  print(a)
if b% 2 == 1 :
  print(b)
if c% 2 == 1 :
  print(c)  

# 34번

a = 3
b = 8
c = 17

if a% 2 == 1 :
  print(a,'홀수')
else :
  print(a,'짝수')
if b% 2 == 1 :
  print(b,'홀수')
else :
  print(b,'짝수')
if c% 2 == 1 :
  print(c,'홀수')
else :
  print(c,'짝수') 

# 35번

n = int(input())

if n > 0:
    if n % 2 == 0:
        print('양수이고 짝수')
    else:
        print('양수이고 홀수')
elif n < 0:
    
     if n % 2 == 0:
        print('음수이고 짝수')
     else:
        print('음수이고 홀수') xx  

# 40번

name = input('이름을 입력하세요:')
n = float(input('키를 입력하세요:'))
if name[0] == 'm' or n >= 150 and n < 170:
    print('탈 수 있어요')
else:
    print('탈 수 없어요')  

# 41번
n = float(input('키를 입력하세요:'))
if(n>=150 and n<170) or(n>=175 and n<=180):
    print('탈 수 있어요')
else:
    print('탈 수 없어요') 

# 42번

n = float(input('키를 입력하세요:'))
m = input('성별을 입력하세요:')
if m == '여자' and ((n>=150 and n<170) or n % 5 ==0):
    print('탈 수 있어요')
else:
    print('탈 수 없어요')  

# 43번

a,b,c = map(int,input().split())
if a>150 and b>150 and c>150:
    print('터널 통과 가능')
else:
    print('터널 통과 불가능') xx 

# 44번

y = int(input('연도를 입력하세요:'))
if (y % 4 == 0 and y % 100 != 0) or (y % 400 ==0):
    print(y,'년은 366일 윤년 입니다')
else:
    print(y,'년은 365일 윤년이 아닙니다')  

# 45번

n = input('주민등록번호 입력:')

century = 20
gender = 'male'

if int(n[7]) <= 2:
    century = 19

if int(n[7]) % 2 == 0:
    gender = 'female'

if gender == 'male':
    print('남자',str(century)+n[:2],'년출생')
else:
    print('여자',str(century)+n[:2],'년 출생') 

# 46번

n = input().split()
m = n.count('1')
if m == 1:
    print('도')
elif m == 2:
    print('개')
elif m == 3:
    print('걸')
elif m == 4:
    print('윳')
else:
    print('모') xx 

# 47번

height,weight = map(float,input().split())

height = height / 100
bmi = weight / (height*height)

if bmi < 18.5:
    print('BMI 지수는',bmi,'이고 저체중입니다')
elif bmi <= 22.9:
    print('BMI 지수는',bmi,'이고 정상중입니다')
elif bmi <= 24.9:
    print('BMI 지수는',bmi,'이고 과체중입니다')
elif bmi <= 29.9:
    print('BMI 지수는',bmi,'이고 경도비만입니다')
else:
    print('BMI 지수는',bmi,'이고 고도비만입니다') xx 

# 48번

a = list(map(int,input().split()))

max_value = max(a)
idx = a.index(max_value)
del a[idx]

if max_value<sum(a):
    print('삼각형 가능')
else:
    print('삼각형 불가')  xx 

# 49번

for i in range(1,11):
    print(i,end=(' '))
print('발사!') 

# 50번

i = 1
while i < 11:
    print(i,end=(" "))
    i += 1
print('발사!') 

i = 7
while i < 16:
    print(i)
    i += 1 
         
i = 7
while i < 36:
    print(i)
    i += 3 

# 51번

n = int(input('카운트다운 몇초전인가요?'))
for i in range(n,0,-1):
    print(i,end=(' '))
print('발사!') 

# 52번

n = int(10)
sum = 0
for i in range(1,n+1):
    sum += i
print('1부터',n,'까지 모두 더한 합은',sum) 

cnt = 0
for i in range(1,101):
    i = str(i)
    if i[-1] == '3' or i[-1] == '6' or i[-1] == '9':
        print('박수치는 숫자',i)
        cnt += 1


# 53번

# 초기값 설정
total = 0
num = 1

# while 루프를 사용하여 합 구하기
while num <= 100:
    total += num
    num += 1

# 결과 출력
print("1부터 100까지의 합은:", total)


# 54번 

while True:  # 무한 반복
    num = int(input("숫자를 입력하세요: "))  # 사용자로부터 숫자 입력 받기
    if num >= 0:  # 입력된 숫자가 0보다 크거나 같은 경우
        print("입력된 수:", num)  # 입력된 수 출력
    else:  # 입력된 숫자가 음수인 경우
        print("프로그램을 종료합니다.")  # 프로그램 종료 메시지 출력
        break  # 반복문 종료

        

while True:
    name = input("이름을 입력하세요 :  ")
    if name != 'end':
        print('안녕하세요', name,'님')
    else:
        print('종료합니다') 
        break   
 


print('makit', end = ' ')
print('woojin')

for i in range(1, 11):
    print(i, end = ' ')

a = 'makit'

for i in range(3):
    print('makit', end = ' $$$ ')

    '''

# 56번

n1 = int(input('첫 번재 숫자르 입력하세요'))
n2 = int(input('두 번재 숫자르 입력하세요'))

sum = 0

for i in range(n1, n2 + 1):
    sum += i
    if i != n2:
        print(i, end = ' + ')
    else:
        print(i, end = '')
print('=', sum)
