import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='park5479##', db='soloDB', charset='utf8')
cur = conn.cursor()
cur.execute('CREATE TABLE userTABLE(id CHAR(4), userName CHAR(15), email CHAR(20), birthYear INT)')

cur.execute("INSERT INTO userTABLE VALUES('hong', '홍지윤', 'hong@naver.com', 1996)")
cur.execute("INSERT INTO userTABLE VALUES('kim', '김태연', 'kim@daum.net', 2011)")
cur.execute("INSERT INTO userTABLE VALUES('star', '별사랑', 'star@paran.com', 1990)")
cur.execute("INSERT INTO userTABLE VALUES('yang', '양지은', 'yang@gmail.com', 1993)")

conn.commit()
conn.close()
