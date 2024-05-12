a ={"주간1" :"무명인","주간2" :"이재평","야간1" :"무명인","야간2" :"안경국","휴무1" :"이성용","휴무2" :"엑스맨","휴무3" :"무명인"}
b ={"주간1" :"무명인","주간2" :"이성용","야간1" :"무명인","야간2" :"엑스맨","휴무1" :"이재평","휴무2" :"안경국","휴무3" :"무명인"}
c ={"주간1" :"안경국","주간2" :"이성용","야간1" :"이재평","야간2" :"엑스맨","휴무1" :"무명인","휴무2" :"무명인","휴무3" :"무명인"}
d ={"주간1" :"안경국","주간2" :"무명인","야간1" :"이재평","야간2" :"무명인","휴무1" :"이성용","휴무2" :"엑스맨","휴무3" :"무명인"}
e ={"주간1" :"엑스맨","주간2" :"무명인","야간1" :"이성용","야간2" :"무명인","휴무1" :"이재평","휴무2" :"안경국","휴무3" :"무명인"}
f ={"주간1" :"엑스맨","주간2" :"이재평","야간1" :"이성용","야간2" :"안경국","휴무1" :"무명인","휴무2" :"무명인","휴무3" :"무명인"}
g ={"주간1" :"무명인","주간2" :"이재평","야간1" :"무명인","야간2" :"안경국","휴무1" :"이성용","휴무2" :"엑스맨","휴무3" :"무명인"}






data = [a, b, c, d, e, f, g]

# a ->x c, b ->x a, c ->x b,    
# a ->x h, b ->x g, c ->x i   
# d ->x b, e ->x a, f ->x c  
# d ->x i, e ->x g, f ->x h
# g ->x i, g ->x b
# h->x g, h->x a
# i ->x h, i ->x c

'''for i in range(len(data)):
    if "무명인" not in data[i].values():
        print(data[i]) ''' 


for _ in range(1):
  
  print(data[data.index(a)])
  print(data[data.index(a)]) 
  
  
for _ in range(2):
  
  print(data[data.index(b)])   
  print(data[data.index(c)])
  print(data[data.index(d)])
  print(data[data.index(e)])
  print(data[data.index(f)])
  print(data[data.index(g)])
  
for _ in range(1):
  
  print(data[data.index(b)])   
  print(data[data.index(c)])
  print(data[data.index(d)])
  print(data[data.index(e)])
  print(data[data.index(f)])

for _ in range(1):
  
  print(data[data.index(a)])
  print(data[data.index(b)])   
  print(data[data.index(c)])
  print(data[data.index(d)])
  print(data[data.index(e)])
  print(data[data.index(f)])
  print(data[data.index(g)])   

for _ in range(1):
  
  print(data[data.index(b)])   
  print(data[data.index(c)])
  print(data[data.index(d)])
  print(data[data.index(e)]) 
  print(data[data.index(f)]) 

