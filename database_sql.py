# DB 생성
# CREATE DATABASE gangnam CHARACTER SET utf8 COLLATE utf8_general_ci;


# topic table 생성
#    CREATE TABLE `topic` (
#        `id` int(11) NOT NULL AUTO_INCREMENT,
#        `title` varchar(100) NOT NULL,
#        `description` text NOT NULL,
#        `author` varchar(30) NOT NULL,
#        PRIMARY KEY (id)
#        ) ENGINE=innoDB DEFAULT CHARSET=utf8;


import pymysql

db = pymysql.connect(
        host='localhost',
        user='root',
        password='1234',
        db='gangnam',
        charset='utf8mb4')

cur = db.cursor()

query = "SELECT * FROM topic"
#cur.execute(query)
#db.commit()

#data = cur.fetchall()

#print(data[0][2])

#print(data[0][2], split(' '))

#추가
#query= 'INSERT INTO `gangnam`.`topic` (`id`, `title`, `description`, `author`) VALUES (2 ,"자바" ,"처음에는 가전제품 내에 탑재해 동작하는 프로그램을 위해 개발했지만 현재 웹 애플리케이션 개발에 가장 많이 사용하는 언어 가운데 하나이고, 모바일 기기용 소프트웨어 개발에도 널리 사용하고 있다. 현재 버전 15까지 출시했다.", "GARY");'
#수정
#query = "UPDATE `gangnam`.`topic` SET `title` = 'dfaf', `description` = '처음에는 가전제품 내에 탑재해 동작하는 프로그램을 위해 개발했지만 현재 웹 애플리케이션 개발에 가장 많이 사용하는 언어 가운데 하나이고, 모바일 기기용 소프트웨어 개발에도 널리 사용하고 있다. 현dsfs재 버전 15까지 출시했다.' WHERE (`id` = '2');"
#삭제
query = "DELETE FROM `gangnam`.`topic` WHERE (`id` = '2');"

cur.execute(query)

db.commit()

db.close()