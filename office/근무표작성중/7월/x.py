
a = {'주간': '박병훈', '야간': '권헌일', '휴무1': '이영재', '휴무2': '엑스맨'}
b = {'주간': '이영재', '야간': '박병훈', '휴무1': '권헌일', '휴무2': '엑스맨'}
c = {'주간': '권헌일', '야간': '이영재', '휴무1': '박병훈', '휴무2': '엑스맨'}
d = {'주간': '소장님', '야간': '이영재', '휴무1': '박병훈', '휴무2': '권헌일'}
e = {'주간': '소장님', '야간': '박병훈', '휴무1': '권헌일', '휴무2': '이영재'}
f = {'주간': '소장님', '야간': '권헌일', '휴무1': '이영재', '휴무2': '박병훈'}
g = {'주간': '박병훈', '야간': '이영재', '휴무1': '권헌일', '휴무2': '엑스맨'}
h = {'주간': '권헌일', '야간': '박병훈', '휴무1': '이영재', '휴무2': '엑스맨'}
i = {'주간': '이영재', '야간': '권헌일', '휴무1': '박병훈', '휴무2': '엑스맨'}


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
  print(data[data.index(h)])  
  
for _ in range(1):

  print(data[data.index(i)])   
  print(data[data.index(i)])  
  print(data[data.index(d)])  
  print(data[data.index(f)])  
  print(data[data.index(d)])  # 10
  
for _ in range(1):  
  
  print(data[data.index(h)])
  print(data[data.index(i)])
  print(data[data.index(i)])
  print(data[data.index(i)])    
  print(data[data.index(g)])    
  print(data[data.index(g)]) 

for _ in range(1):  
  
  print(data[data.index(h)])
  print(data[data.index(i)])
  print(data[data.index(i)])
  print(data[data.index(i)])    
  print(data[data.index(g)])    
  print(data[data.index(g)])  # 22 

for _ in range(1):  
  
  print(data[data.index(h)])
  print(data[data.index(h)]) 
  print(data[data.index(i)])
  print(data[data.index(i)])    
  print(data[data.index(g)])    
  print(data[data.index(g)])         
  
for _ in range(1):  
  
  print(data[data.index(g)])
  print(data[data.index(h)])
  print(data[data.index(h)])

  





 


