"""
pymysql操作数据库基本流程演示
"""

import pymysql

# 连接数据库
db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                   password='123456',
                   database='student',
                   charset='utf8')

# 获取游标（操作数据库，执行sql语句）
cur=db.cursor()

# 执行sql语句---(;)可不写
sql="insert into class values (6,'Emma',17,'w',76.5,'2019-8-8');"

# 执行语句
cur.execute(sql)

# 将写操作提交，多次写操作一同提交
db.commit()

# 关闭数据库
cur.close()
db.close()

