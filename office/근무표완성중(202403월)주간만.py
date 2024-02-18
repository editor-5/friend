
a = {'주간1': '황인기', '주간2': '유현주', '휴무': '      '}
b = {'주간1': '황인기', '주간2': '      ', '휴무': '유현주'}
c = {'주간1': '      ', '주간2': '유현주', '휴무': '황인기'}

data = [a, b, c]

for _ in range(3):

  print(data[data.index(c)])   #1
  
for _ in range(1):
  
  print(data[data.index(a)])   #4
  print(data[data.index(b)])   #5
    
for _ in range(4):

  print(data[data.index(a)])   #6
  
for _ in range(1):

  print(data[data.index(c)])  #10
  print(data[data.index(a)])  #11
  print(data[data.index(b)])  #12
   
for _ in range(3):

  print(data[data.index(a)])  #13
   
for _ in range(1):

  print(data[data.index(b)])  #16
  print(data[data.index(c)])  #17 
  print(data[data.index(a)])  #18
  print(data[data.index(b)])  #19 

for _ in range(4):

  print(data[data.index(a)])  #20     

for _ in range(1):

  print(data[data.index(c)])  #24
  print(data[data.index(a)])  #25 
  print(data[data.index(b)])  #26 
  print(data[data.index(a)])  #27
  print(data[data.index(b)])  #28  
  print(data[data.index(a)])  #29
  print(data[data.index(a)])  #30
  print(data[data.index(c)])  #31