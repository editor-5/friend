
'''a =  "='[일마감22.01월.xlsx]" 
b = '('
c = 2
d = ")'!$F$13"

f = a + b + str(c) + d  
 
 
print(f) '''

a = "='[일마감23.12월.xlsx]"
b = '('
d = ")'!$F$13"

# c값을 변경하면서 f를 출력
for c in range(1, 32):
    f = a + b + str(c) + d
    print(f)
