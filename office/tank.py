a = float(input(" %를 입력하세요 : "))  # Convert input to a float
pliter = 61672
pper = 100
pkg = 36042
pmm = 3500
pm3 = 61.716
pL = 61716

per = ((a * 0.36) + 20) / 0.36
if per > 90.5 :
    print (" 이충전 작업 하지마세요")
else :    
    print(f"per: {round(per, 1)}")

liter = (pliter * a) / pper  # Perform the calculation
print(f"liter: {round(liter, 1)}")

kg = (pkg * per) / pper
print(f"kg: {round(kg, 1)}")

mm = (pmm * a) / 100
print(f"mm: {round(mm, 1)}")

m3 = (pm3 * a) / 100
print(f"m3: {round(m3, 1)}")

L = (pL * a) / 100
print(f"L: {round(L, 1)}")

print('HH - 94.1 , H - 90.5 , L - 17.8 , LL - 16.3')




