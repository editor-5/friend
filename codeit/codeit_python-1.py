'''
# 2의 n제곱"을 출력하는 프로그램을 만들려고 합니다.

# 코드를 실행하면 아래와 같이 2^0 = 1부터 2^10 = 1024까지 출력되어야 합니다.

def print_powers_of_two(n):
    for i in range(n + 1):
        print(f"2^{i} = {2**i}")

print_powers_of_two(10)

# 구구단 프로그램을 while문이 아닌 for문을 사용해서 만들어 보세요.

for i in range(1, 10):
    for j in range(1, 10):
        print("{} * {} = {}".format(i, j, i * j))

# 피타고라스
for a in range(1, 400):
    for b in range(1, 400):
        c = 400 - a - b
        if a * a + b * b == c * c and a < b < c:
            print(a * b * c)

numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
for left in range(len(numbers) // 2):
    # 인덱스 left와 대칭인 인덱스 right 계산
    right = len(numbers) - left - 1

    # 위치 바꾸기
    temp = numbers[left]
    numbers[left] = numbers[right]
    numbers[right] = temp

print("뒤집어진 리스트: " + str(numbers))

# 위에-1
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

for i in range(len(numbers) // 2):
    # 리스트의 첫 번째와 마지막 요소부터 순서대로 바꿉니다.
    temp = numbers[i]
    numbers[i] = numbers[-i - 1]
    numbers[-i - 1] = temp

print(numbers) 

# 단어장 만들기
vocab = {
    "sanitizer": "살균제",
    "ambition": "야망",
    "conscience": "양심",
    "civilization": "문명"
}

# 새로운 단어들 추가
vocab["privilege"] = "특권"
vocab["principle"] = "원칙"

print(vocab)  

def reverse_dict(dictionary):
    return {v: k for k, v in dictionary.items()}

# 영-한 단어장
vocab = {
    "sanitizer": "살균제",
    "ambition": "야망",
    "conscience": "양심",
    "civilization": "문명",
    "privilege": "특권",
    "principles": "원칙"
}
print("영-한 단어장")
print(vocab)

# 한-영 단어장
reversed_vocab = reverse_dict(vocab)
print("\n한-영 단어장")
print(reversed_vocab) 

# 투표 결과 리스트
votes = ['김영자', '강승기', '최만수', '김영자', '강승기', '강승기', '최만수', '김영자', \
'최만수', '김영자', '최만수', '김영자', '김영자', '최만수', '최만수', '최만수', '강승기', \
'강승기', '김영자', '김영자', '최만수', '김영자', '김영자', '강승기', '김영자']

# 후보별 득표수 사전
vote_counter = {}

# 리스트 votes를 이용해서 사전 vote_counter를 정리하기
for name in votes:
    if name not in vote_counter:
        vote_counter[name] = 1
    else:
        vote_counter[name] += 1

# 후보별 득표수 출력
print(vote_counter) 

def sum_digit(num):
    """
    정수형 num의 각 자릿수를 더한 값을 반환하는 함수
    """
    # 각 자릿수를 더할 변수 초기화
    total = 0
    
    # 각 자릿수를 더함
    while num > 0:
        total += num % 10  # num을 10으로 나눈 나머지를 더함
        num //= 10  # num을 10으로 나눈 몫을 다음 숫자로 업데이트
    
    return total

# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
result_sum = sum(sum_digit(num) for num in range(1, 1001))
print(result_sum) 

def mask_security_number(security_number):
    return security_number[:-4] + '****'


# 테스트
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111")) 

def is_palindrome(word):
    """
    주어진 문자열이 팰린드롬인지 확인하는 함수
    """
    # 문자열을 뒤집어서 비교하여 팰린드롬 여부를 확인
    return word == word[::-1]

# 테스트
words = ["racecar", "hello", "토마토", "기러기", "python"]
for word in words:
    print(is_palindrome(word)) 

import random

# 상수 정의
ANSWER = random.randint(1, 20)
NUM_TRIES = 4

# 변수 정의
guess = -1
tries = 0

while guess != ANSWER and tries < NUM_TRIES:
    guess = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: ".format(NUM_TRIES - tries)))
    tries += 1    
    
    if ANSWER > guess:
        print("Up")
    elif ANSWER < guess:
        print("Down")

if guess == ANSWER:
    print("축하합니다. {}번 만에 숫자를 맞히셨습니다.".format(tries))
else:
    print("아쉽습니다. 정답은 {}입니다.".format(ANSWER))  

with open('test2.txt', 'r') as f:
    for line in f:
        print(line.strip())  

full_name = "Kim, Yuna"
print(full_name.split(", "))  

full_name = "Kim, Yuna"
name_data = full_name.split(", ")
last_name = name_data[0]
first_name = name_data[1]

print(first_name, last_name) 

numbers = "     \n\n     2   \t  3   \n  5 7 11  \n\n".split()
print(int(numbers[0]) + int(numbers[1])) 



with open('data/chicken.txt', 'r') as f:
    total_revenue = 0
    total_days = 0
    
    for line in f:
        data = line.strip().split(": ")
        revenue = int(data[1])  # 그날의 매출

        total_revenue += revenue
        total_days += 1

    print(total_revenue / total_days)  
 
with open('test3.txt', 'a') as f:
    f.write("Hello world!")
    f.write("My name is Codeit.")  

with open('vocabulary.txt', 'w') as f:
    while True:
        english_word = input('영어 단어를 입력하세요: ')    
        if english_word == 'q':
            break
        
        korean_word = input('한국어 뜻을 입력하세요: ')
        if korean_word == 'q':
            break
        
        f.write('{}: {}\n'.format(english_word, korean_word)) 

with open('vocabulary.txt', 'r') as f:
    for line in f:
        data = line.strip().split(": ")
        english_word, korean_word = data[0], data[1]
        
        # 유저 입력값 받기
        guess = input("{}: ".format(korean_word))
        
        # 정답 확인하기
        if guess == english_word:
            print("맞았습니다!\n")
        else:
            print("아쉽습니다. 정답은 {}입니다.\n".format(english_word)) 

import random

# 사전 만들기
vocab = {}
with open('vocabulary.txt', 'r') as f:
    for line in f:
        data = line.strip().split(": ")
        english_word, korean_word = data[0], data[1]
        vocab[english_word] = korean_word

# 목록 가져오기
keys = list(vocab.keys())

# 문제 내기
while True:
    # 랜덤한 문제 받아 오기
    index = random.randint(0, len(keys) - 1)
    english_word = keys[index]
    korean_word = vocab[english_word]
    
    # 유저 입력값 받기
    guess = input("{}: ".format(korean_word))
    
    # 프로그램 끝내기
    if guess == 'q':
        break
    
    # 정답 확인하기
    if guess == english_word:
        print("정답입니다!\n")
    else:
        print("틀렸습니다. 정답은 {}입니다.\n".format(english_word))  

from random import randint


def generate_numbers(n):
    numbers = []

    while len(numbers) < n:
        num = randint(1, 45)
        if num not in numbers:
            numbers.append(num)

    return numbers


# 테스트 코드
print(generate_numbers(6))  


from random import randint


def generate_numbers(n):
    numbers = []

    while len(numbers) < n:
        num = randint(1, 45)
        if num not in numbers:
            numbers.append(num)

    return numbers


def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]


# 테스트 코드
print(draw_winning_numbers())  

def count_matching_numbers(numbers, winning_numbers):
    count = 0

    for num in numbers:
        if num in winning_numbers:
            count = count + 1

    return count


# 테스트 코드
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14])) 

def count_matching_numbers(numbers, winning_numbers):
    count = 0

    for num in numbers:
        if num in winning_numbers:
            count = count + 1

    return count


def check(numbers, winning_numbers):
    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])

    if count == 6:
        return 1000000000
    elif count == 5 and bonus_count == 1:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0


# 테스트 코드
print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25])) 

from random import randint


def generate_numbers():
    numbers = []

    while len(numbers) < 3:
        num = randint(0, 9)
        if num not in numbers:
            numbers.append(num)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


# 테스트 코드
print(generate_numbers()) 

def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    while len(new_guess) < 3:
        new_num = int(input("{}번째 숫자를 입력하세요: ".format(len(new_guess) + 1)))

        if new_num < 0 or new_num > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif new_num in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            new_guess.append(new_num)

    return new_guess
  
    
# 테스트 코드
print(take_guess()) 

def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0

    for i in range(3):
        if guesses[i] == solution[i]:
            strike_count += 1
        elif guesses[i] in solution:
            ball_count += 1

    return strike_count, ball_count


# 테스트 코드
s_1, b_1 = get_score([2, 7, 4], [2, 4, 7])
print(s_1, b_1)

s_2, b_2 = get_score([7, 2, 4], [2, 4, 7])
print(s_2, b_2)

s_3, b_3 = get_score([0, 4, 7], [2, 4, 7])
print(s_3, b_3)

s_4, b_4 = get_score([2, 4, 7], [2, 4, 7])
print(s_4, b_4) 

from random import randint


def generate_numbers():
    numbers = []

    while len(numbers) < 3:
        new_number = randint(0, 9)
        if new_number not in numbers:
            numbers.append(new_number)

    return numbers


def take_guess():
    new_guess = []
    while len(new_guess) < 3:
        num = int(input("{}번째 수를 입력하세요: ".format(len(new_guess) + 1)))

        if num < 0 or num > 9:
            print("0에서 9까지의 수를 입력해 주세요!")
        elif num in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            new_guess.append(num)

    return new_guess


def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0

    for i in range(3):
        if guesses[i] == solution[i]:
            strike_count += 1
        elif guesses[i] in solution:
            ball_count += 1

    return strike_count, ball_count


# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

while True:
    user_guess = take_guess()
    s, b = get_score(user_guess, ANSWER)

    print("{}S {}B\n".format(s, b))
    tries += 1

    if s == 3:
        break

print("축하합니다. {}번 만에 세 숫자의 값과 위치를 모두 맞히셨습니다.".format(tries)) 
 '''
























