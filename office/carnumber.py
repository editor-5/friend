car_number = input("차량번호를 입력하세요")
a = [1368,1401,1426,1590,1646,1939,2124,2171,2198,2200,2214,2275,2296,2332,2387,2484,2618,2628,
    2671,2815,2991,2992,3022,3048,3556,3721,3767,3843,3921,4106,4341,4506,4615,4694,4906,4989,5325,
    5404,5414,5551,5787,5809,5866,5874,5899,5907,6129,6265,6372,6409,6435,6462,6534,6898,7079,7439,
    7378,7439,7488,7816,8058,8112,8130,8289,8300,8331,8386,8403,8420,8421,8587,9491,9700,9772,9785,9983,7211,7257,7357,7378,7439,8130,6380,1157,6518,7211,7257,7357,7309]

# 입력값을 정수로 변환하여 리스트에 있는지 확인
if int(car_number) in a:
    print("등록번호입니다")
else:
    print("아닙니다")

    
