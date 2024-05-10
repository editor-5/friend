
a = {'주간': '이성용', '야간': '이재평', '휴무1': '안경국', '휴무2': '엑스맨'}
b = {'주간': '안경국', '야간': '이성용', '휴무1': '이재평', '휴무2': '엑스맨'}
c = {'주간': '이재평', '야간': '안경국', '휴무1': '이성용', '휴무2': '엑스맨'}
d = {'주간': '유현주', '야간': '이재평', '휴무1': '이성용', '휴무2': '안경국'}
e = {'주간': '유현주', '야간': '이성용', '휴무1': '안경국', '휴무2': '이재평'}
f = {'주간': '유현주', '야간': '안경국', '휴무1': '이재평', '휴무2': '이성용'}
g = {'주간': '이성용', '야간': '안경국', '휴무1': '이재평', '휴무2': '엑스맨'}
h = {'주간': '이재평', '야간': '이성용', '휴무1': '안경국', '휴무2': '엑스맨'}
i = {'주간': '안경국', '야간': '이재평', '휴무1': '이성용', '휴무2': '엑스맨'}

data = [a, b, c, d, e, f, g, h, i]

# a ->x c, b ->x a, c ->x b,    
# a ->x h, b ->x g, c ->x i   
# d ->x b, e ->x a, f ->x c  
# d ->x i, e ->x g, f ->x h
# g ->x i, g ->x b
# h->x g, h->x a
# i ->x h, i ->x c

  
for _ in range(1):
  
  print(data[data.index(a)])
  print(data[data.index(b)]) 
  print(data[data.index(b)])   
  print(data[data.index(b)])
  print(data[data.index(c)])
  print(data[data.index(c)])
  
for _ in range(1):
  
  print(data[data.index(a)])
  print(data[data.index(a)]) 
  print(data[data.index(b)])   
  print(data[data.index(b)])
  print(data[data.index(c)])
  print(data[data.index(c)])

for _ in range(3):
  
  print(data[data.index(a)])
  print(data[data.index(a)]) 
  print(data[data.index(b)])   
  print(data[data.index(b)])
  print(data[data.index(c)])
  print(data[data.index(c)])

for _ in range(1):
  
  print(data[data.index(a)]) 
  
  
