
'''
# 산소의 분압= (산소의 양 / 전체 공기의 양 × 총 압력)
# 산소의 분압= 4L / 4L × 1 기압 
# 산소의 분압=1 기압 

O = 0.2  # 산소비율 백분율
air = 20  
psi = 1   
yonggi = 4  

dab = (air * O ) / yonggi * psi

print(dab)

# 25

내용적 = 117.5
액화프로판 = 50
LPG비중 = "20도에서 0.5프로"
 
LPGVIGUNG = 50 / 117.5
LPGVUPI = 50 / 0.425
LPGVIUL = (LPGVUPI-내용적)/LPGVUPI

print(LPGVIGUNG)
print(LPGVUPI)
print(LPGVIUL)


# 26
W = 500
V = 50
C = 0.98

dab =  W * C / V
print(dab)



# 40
LPG = 44
V = 22.4
LPG1 = 92
V1 = V * LPG1 / LPG
print(V1)



# 41

BI = 0.8
LH = 8
SUBI = 13.6
SUH = LH * BI / SUBI * 1000
print(SUH)

# 42 (정답 1.679 kg/cm2) - 재검토요망

P1 = 1
H = 500
P2 = (P1 + 1.033) * H / 760  # P1 + H
print(P2)

# 43  W = C / V
W = 500
V1 = 50
C = 0.8
V = W * C
YOGI = V / V1
print(YOGI)

# 44 압력 = 밀도 * 중력 * 높이 =   pa
VI = 2.5
H = 6
P = VI * H
print(P)

# 50 
KC = 3
LBIN = 14.2233
KC1 = KC * LBIN
print(KC1)

# 51 절대압력 = 대기압 - 진공압(주어진압력) , 대기압 - 센티미터수은주(26 / 73.5) = 상대압력 
#              0.353은 대기압에서 뺀 상대압력을 나타냄 
CMHGV = 26
CMHG = 73.5
SANGP = CMHGV / CMHG
KGCM2A = 1.033 - SANGP
print(KGCM2A)

# 53   30 값은 알아봐야함
INHG = 20
LB = 14.7
X = 30
LBIN2A = LB - (LB * INHG / X)
print(LBIN2A)

# 54 (샤르의법칙) 
K = 273
T1 = 20 
V1 = 1
V2 = V1 * 2 
T2 = (T1 * V2 / V1) + K
print(T2)

# 59 (보일의법칙)
PA = 1 
P1 = 1
V1 = 1.5 * 1000  # M3
V2 = 40  # L
P2 = P1 * V1 / V2
print(P2)

# 61 ( 액체 1L 는 가스 250L)
GA = 250
LPG = 20
C = 0.5
L = LPG / C
G = GA * L / 1000  # M3
print(G)

'''
# 62 (샤르의법칙)
K = 273
T1 = 15 
V1 = 1
V2 = V1 * 2 
T2 = (T1 * V2 / V1) + K
print(T2)

# 64 (보일샤르의법칙)
K = 273
T1 = 20 + K 
P1 = 100
P2 = 350 * ( 8 / 10 )
T2 = (T1 * P2 / P1) - K  
print(T2)

# 65
V = 50
P = 150
S1 = 300
S2 = V * P / S1
print(S2) 

# 66 (보일샤르의법칙)
K = 273
T1 = 15 + K 
P1 = 130
T2 = 50 + K
P2 = (P1 * T2 / T1)   
print(P2)

# 67 (보일샤르의법칙)
K = 273
T1 = 20 + K 
P1 = 1
T2 = 80 + K
P2 = (P1 * T2 / T1)   
print(P2)

# 71 Q = W * C * T (온도차)
W = 0.113
C = 200
TS = 85 - 20
Q = W * C * TS
print(Q)

# 77
LPG = 16
DO = -42.6
DOSIBAL = 700
LPGGI1 = 95
LPGGI2 = 80
KG = (LPG * LPGGI1) / (DOSIBAL * LPGGI2 * 0.01)
print(KG)

# 79 PV = GRT  , V = GRT / P
G = 100  # KG
R = 26.5 # 산소의 가스정수
T = 20 + 273 
P = (120 + 1.033 )* (10**4)
V = (G * R * T) / P
print(V)

# 88 (보일의법칙) P1*V1 = P2*V2 , P2= P1*V1 / V2
PA = 1 
P1 = 5
V1 = 20  # L
V2 = 60  # L
P2 = P1 * V1 / V2
print(P2)

# 89 (보일의법칙) P1 * V1 = P2 * V2 , V2 = P1 * V1 / P2
TA = 25 
P1 = 4
P2 = 2
V1 = 100 # L
V2 = P1 * V1 / P2 
print(V2)






