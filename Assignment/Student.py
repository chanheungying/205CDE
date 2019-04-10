from flask import Flask
import pymysql
app = Flask(__name__)

import pymysql.cursors

db = pymysql.connect(host='localhost',
                     user='phpmyadmin',
                     password='20160715',
                     db='205CDE',
                     charset='utf8mb4',
                     cursorclass=pymysql.cursors.DictCursor)

cursor =db.cursor()

try:
        sql = "INSERT INTO `Lab` (`user`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
        db.commit()

        sql = "SELECT `id`, `password` FROM `Lab` WHERE `id`=1"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)


finally:
    db.close()