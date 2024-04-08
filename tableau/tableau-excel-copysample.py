
'''
# 충전금액

a = "='[일마감24.03월.xlsx]"
b = '('
d = ")'!$K$13"

# c값을 변경하면서 f를 출력
for c in range(1, 32):
    f = a + b + str(c) + d
    print(f)

'''

# CAR WASH

a = "='[일마감24.03월.xlsx]"
b = '('
d = ")'!$P$24"

# c값을 변경하면서 f를 출력
for c in range(1, 32):
    f = a + b + str(c) + d
    print(f)
    