
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

for _ in range(5):

  print(data[data.index(c)])   
  print(data[data.index(c)])
  print(data[data.index(a)])   
  print(data[data.index(a)])
  print(data[data.index(b)])
  print(data[data.index(b)])



