import random

def generate_lotto_numbers():
    # 1부터 45까지의 숫자 리스트 생성
    numbers = list(range(1, 46))
    # 랜덤으로 6개의 숫자 추출 (중복 없음)
    lotto_numbers = random.sample(numbers, 6)
    # 추출된 숫자 정렬
    lotto_numbers.sort()
    return lotto_numbers

if __name__ == "__main__":
    lotto_numbers = generate_lotto_numbers()
    print("로또 번호:", lotto_numbers)
