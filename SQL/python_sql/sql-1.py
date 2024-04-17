import pymysql

# 전역변수 선언부
conn, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
Sql = ""

# 메인 코드
conn = pymysql.connect(host='127.0.0.1', user='root', password='park5479##', db='soloDB', charset='utf8')
cur = conn.cursor()

while True:
    data1 = input("사용자ID==> ")
    if data1 == "":
        break

    data2 = input("사용자 이름 ==>")
    data3 = input("사용자 이메일 ==>")
    data4 = input("사용자 출생연도 ==>")
    Sql = "INSERT INTO usertable VALUES('" + data1 + "','" + data2 + "','" + data3 + "'," + data4 + ")"
    cur.execute(Sql)  # Execute the SQL query inside the loop

conn.commit()
conn.close()




'''
import pymysql

# 전역변수 선언부
conn,cur=None.None
data1, data2,data3, deta4 = "","","",""
sql = ""

# 메인 코드
conn = pymysql.connect(host = '127.0.0.1', user = 'root^', passwvord = 'park5479##' db = 'soloDE', charsect= 'utf8')
cur = conn.cursor()

while (True) :
deta1 = input("사용자1D==> ")
if deta1 == ""
    break;

data2 = input("사용자 이름 ==>")
data3 = input("사용자 이메일 ==>")
deta4 = input("사용자 출생연도 ==>")
SqI = "INSERT INTO userTable VALUES('" + data1 + "','" + data2 + "','" + data3 + "'," + data4 + ")"
cur.execute(sql)

conn.commit()
conn.close()

'''
