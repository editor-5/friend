
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

#90 (보일샬의법칙)  P1V1/T1 = P2V2/T2  
P1 = 0
V1 = 600
T1 = 27 + 273
P2 = 0
T2 = 127 + 273
V2 = (V1 * T2) / T1
print(V2)

# 91 (보일샬의법칙)  P1V1/T1 = P2V2/T2  
P1 = 2
V1 = 4
T1 = 27 + 273
P2 = 1
T2 = 0 + 273
V2 = (P1 * V1 * T2) / (P2 * T1)
print(V2)

#92 PV = NRT , PV = W/M R T , P = M R T / V W
W = 26 
R = 0.082
T = 10 + 273
M = 2 
V = 28.3
P = (W * R * T) / (M * V)
print(P)

#93 PV = NRT , PV = W/M R T , P = M R T / V W , P = NRT / V
W = 0 
R = 0.082
T = 200 + 273
M = 0
NH = 8.4
NN = 2
H2 = 1
N2 = 14
N = (8.4 / 28) + (2 / 2) 
V = 1
P = (N * R * T) /  V
print(P)

#94 PV = NRT , PV = W/M R T , P = M R T / V W , P = NRT / V ,  M = P V W / R T
W = 30
R = 0.082
T = 20 + 273
P = 1
V = 10
M = (R * T * W) / (P * V)
print(M)

#96 PV = NRT , PV = W/M R T , P = M R T / V W , P = NRT / V ,  M = P V W / R T , P = MM R T / M
W = 0
R = 0.082
T = 27 + 273
P = 1
V = 0
MM = 1.3
M = (MM * R * T) / P
print(M)   # 산소 16 * 2 = O2

# 115 진공도 = 진공압 * 100 / 대기압 
진공압 = 0.8
대기압 = 700
KGCM = 0.00131578947 
진공도 = (진공압 * 100) / (대기압 * KGCM)
print(진공도)
print(대기압 * KGCM)

# 127  (보일의법칙) P1 V1 = P2 V2
P1 = 1
V1 = 10
V2 = 300
P2 = (P1 * V1) / V2
print(P2)

# 128  (보일의법칙) P1 V1 = P2 V2
P1 = 1
V1 = 100
V2 = 5
P2 = (P1 * V1) / V2
print(P2)

# 130  (보일샬의법칙) P1 V1 / T1 = P2 V2 / T2 , V2 = V1 P1 T2 / P2 T1
P1 = 1
P2 = 1
T1 = 0 + 273
T2 = 273 + 273
V1 = 4
V2 = (V1 * P1 * T2) / (P2 * T1)
print(V2)

# 131 (전압력)
PN = 2
PO = 3
VN = 4
VO = 4
V = 5
PALL = ((PN * VN) + (PO * VO)) / V
print(PALL)

# 133  (보일의법칙) P1 V1 = P2 V2 , V2 = P1 V1 / P2
P1 = 200
V1 = 20
P2 = 1
V2 = (P1 * V1) / P2
print(V2)

# 134  (샬의법칙) P1 / T1 = P2 / T2 , T2 =  P2 T1 / P1
P1 = 110
P2 = 130
T1 = 30 + 273
V1 = 45
T2 = ( P2 * T1) / P1
print(T2-273)

# 135  
P1 = 2
V1 = 3
T1 = 0 + 273
P2 = 3
T2 = 0 + 273
V2 = 5
V3 = 3
P3 = ((P1 * V1) +(P2 * V2)) / V3
print(P3)

# 137  (보일샬의 법칙) P1 V1 / T1 = P2 V2 /T2 , 
P1 = 2
V1 = 80
T1 = 30 + 273
T2 = 15 + 273
V2 = 4
P2 = ((P1 * V1 * T2) / (T1 * V2)) 
print(P2)

'''

SANGSU = 9/5
C = 0
FSANGSU = 32
F = (SANGSU * C) + FSANGSU
print(F)

SANGSU2 = 5/9
FSANGSU = 32
F = 0
C = SANGSU2 * (F-32)
print(C)

C = 0
KSANGSU = 273
K = C + KSANGSU
print(K)
 
K = 1
RSANGSU = 1.8
R = K * RSANGSU
print(R)

F = 0
RSANGSU1 = 460
R = F + RSANGSU1
print(R)
