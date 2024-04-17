import pymysql

# 전역변수 선언부
conn, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
row = None

# 메인 코드
conn = pymysql.connect(host='127.0.0.1', user='root', password='park5479##', db='soloDB', charset='utf8')
cur = conn.cursor()

cur.execute("SELECT * FROM usertable")

print("사용자ID 사용자 이름 사용자 이메일 사용자 출생연도")
print("------------------------------------------------")

while (True):
    row = cur.fetchone()
    if row == None :
        break

    data1 = row[0]    
    data2 = row[1] 
    data3 = row[2]  
    data4 = row[3]  
    print("%5s %15s %20s %d" % (data1, data2, data3, data4 ))
     
conn.close()