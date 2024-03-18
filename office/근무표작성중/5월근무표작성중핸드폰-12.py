
a = {'주간': '박병훈', '야간': '권헌일', '휴무': '이영재'}
b = {'주간': '이영재', '야간': '박병훈', '휴무': '권헌일'}
c = {'주간': '권헌일', '야간': '이영재', '휴무': '박병훈'}
d = {'주간': '     ', '야간': '이영재', '휴무': '박병훈,권헌일'}
e = {'주간': '     ', '야간': '박병훈', '휴무': '권헌일,이영재'}
f = {'주간': '     ', '야간': '권헌일', '휴무': '이영재,박병훈'}
g = {'주간': '박병훈', '야간': '이영재', '휴무': '권헌일'}
h = {'주간': '권헌일', '야간': '박병훈', '휴무': '이영재'}
i = {'주간': '이영재', '야간': '권헌일', '휴무': '박병훈'}

data = [a, b, c, d, e, f, g, h, i]

# a ->x c, b ->x a, c ->x b,    
# a ->x h, b ->x g, c ->x i   
# d ->x b, e ->x a, f ->x c  
# d ->x i, e ->x g, f ->x h
# g ->x i, g ->x b
# h->x g, h->x a
# i ->x h, i ->x c

for _ in range(1):

  print(data[data.index(c)])   
  

for _ in range(1):

  print(data[data.index(c)])   
  print(data[data.index(c)])
  print(data[data.index(a)])   
  print(data[data.index(a)])
  print(data[data.index(b)])
  print(data[data.index(b)]) 
  
for _ in range(1):

  print(data[data.index(c)])   
  print(data[data.index(c)])
  print(data[data.index(a)])   
  print(data[data.index(a)])
  print(data[data.index(b)])
  print(data[data.index(b)]) 

for _ in range(1):

  print(data[data.index(c)])   
  print(data[data.index(a)])
  print(data[data.index(a)])   
  print(data[data.index(a)])
  print(data[data.index(b)])
  print(data[data.index(b)]) 

for _ in range(1):

  print(data[data.index(c)])   
  print(data[data.index(c)])
  print(data[data.index(a)])   
  print(data[data.index(a)])
  print(data[data.index(b)])
  print(data[data.index(b)]) 

for _ in range(1):

  print(data[data.index(i)])   
  print(data[data.index(g)])
  print(data[data.index(h)])   
  print(data[data.index(i)])
  print(data[data.index(b)])
  print(data[data.index(c)])  
 
'''
# 각 요소가 몇 번 출력되는지를 저장할 딕셔너리를 초기화합니다.
element_count = {'주간': {}, '야간': {}, '휴무': {}}

# 데이터를 순회하며 각 요소의 출현 빈도를 계산합니다.
for d in data:
    for key, value in d.items():
        # 요소가 이미 딕셔너리에 있는 경우, 출현 빈도를 1 증가시킵니다.
        if value.strip() in element_count[key]:
            element_count[key][value.strip()] += 1
        # 요소가 딕셔너리에 없는 경우, 새로운 키로 추가하고 출현 빈도를 1로 초기화합니다.
        else:
            element_count[key][value.strip()] = 1

# 결과를 출력합니다.
for element, counts in element_count.items():
    print(f"{element}별 출현 빈도:")
    for item, count in counts.items():
        print(f"- {item}: {count}번")
        

# 각 요소가 몇 번 출력되는지를 저장할 딕셔너리를 초기화합니다.
element_count = {}

# 데이터를 순회하며 각 요소의 출현 빈도를 계산합니다.
for d in data:
    for key, value in d.items():
        # 요소가 이미 딕셔너리에 있는 경우, 출현 빈도를 1 증가시킵니다.
        if value in element_count:
            element_count[value] += 1
        # 요소가 딕셔너리에 없는 경우, 새로운 키로 추가하고 출현 빈도를 1로 초기화합니다.
        else:
            element_count[value] = 1

# 결과를 출력합니다.
for element, count in element_count.items():
    print(f"'{element}'가 {count}번 출현했습니다.")

'''    


    