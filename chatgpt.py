'''
# 파이썬에서 sort() 함수는 리스트 객체의 메서드로, 리스트의 요소들을 정렬하는 데 사용됩니다. sort() 함수는 원본 리스트를 직접 변경하며, 
# 새로운 정렬된 리스트를 반환하지 않습니다. 이 함수는 기본적으로 리스트의 요소를 오름차순으로 정렬합니다.

my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
my_list.sort()
print(my_list)  # 출력: [1, 1, 2, 3, 4, 5, 5, 6, 9]

my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
my_list.sort(reverse=True)
print(my_list)  # 출력: [9, 6, 5, 5, 4, 3, 2, 1, 1]

# 문자열의 길이를 기준으로 정렬하는 예제
my_list = ['apple', 'banana', 'cherry', 'date']
my_list.sort(key=len)
print(my_list)  # 출력: ['date', 'apple', 'banana', 'cherry']

# 리스트 내부의 리스트를 요소로 가지는 경우
my_list = [[3, 1], [4, 1], [1, 5], [2, 6], [5, 9]]
my_list.sort(key=lambda x: x[1])  # 내부 리스트의 두 번째 요소를 기준으로 정렬
print(my_list)  # 출력: [[3, 1], [4, 1], [1, 5], [5, 9], [2, 6]]

'''


# map() 함수는 파이썬에서 사용되는 내장 함수 중 하나로, 주어진 함수를 순회 가능한(iterable) 
# 객체(예: 리스트, 튜플 등)의 각 요소에 적용하여 새로운 값을 반환합니다. map() 함수는 매우 유용하며
# 코드를 간결하게 작성할 수 있도록 도와줍니다.

# map(function, iterable)

my_list = [1, 2, 3, 4, 5]

# 각 요소를 제곱하는 함수
def square(x):
    return x ** 2

# map() 함수를 사용하여 제곱 함수를 각 요소에 적용
result = map(square, my_list)

# map() 함수는 이터레이터를 반환하므로 결과를 리스트로 변환하여 출력
print(list(result))  # 출력: [1, 4, 9, 16, 25]

my_list = [1, 2, 3, 4, 5]

# map() 함수와 람다(lambda) 함수를 함께 사용
result = map(lambda x: x ** 2, my_list)

print(list(result))  # 출력: [1, 4, 9, 16, 25]



