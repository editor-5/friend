
a = {'주간': '박병훈', '야간': '권헌일', '휴무': '이영재'}
b = {'주간': '이영재', '야간': '박병훈', '휴무': '권헌일'}
c = {'주간': '권헌일', '야간': '이영재', '휴무': '박병훈'}
d = {'주간': '소장님', '야간': '이영재', '휴무': '박병훈,권헌일'}
e = {'주간': '소장님', '야간': '박병훈', '휴무': '권헌일,이영재'}
f = {'주간': '소장님', '야간': '권헌일', '휴무': '이영재,박병훈'}
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

  print(data[data.index(g)])  
  print(data[data.index(g)])
  print(data[data.index(h)])   
  print(data[data.index(h)])
  print(data[data.index(i)])
  print(data[data.index(i)])    
     
  
for _ in range(1):

  print(data[data.index(g)])    
  print(data[data.index(g)])   
  print(data[data.index(g)])
  print(data[data.index(h)])  # 10
  print(data[data.index(h)])
  

for _ in range(1):

  print(data[data.index(i)])    
  print(data[data.index(i)])   
  print(data[data.index(g)])  # 15
  print(data[data.index(g)])   
  print(data[data.index(h)])
  print(data[data.index(h)])
  
for _ in range(1):

  print(data[data.index(i)])    
  print(data[data.index(i)])  # 20
  print(data[data.index(g)]) 
  print(data[data.index(g)])
  print(data[data.index(h)])   
   
  

for _ in range(1):

  print(data[data.index(i)])  # 23 
  print(data[data.index(i)])  # 24 
  print(data[data.index(d)])  # 25 
  print(data[data.index(f)])  # 26
  print(data[data.index(d)])  # 27 
  print(data[data.index(h)])
  print(data[data.index(h)])
  print(data[data.index(i)])    
  print(data[data.index(i)])





 



