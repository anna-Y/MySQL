"""
单词本存入数据库
"""

import re
import pymysql
f=open('dict.txt')

# 连接数据库
db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                   password='123456',
                   database='student1',
                   charset='utf8')

# 获取游标（操作数据库，执行sql语句）
cur=db.cursor()

# data=f.readline()
# tmp = data.split(' ')
# print(tmp)
# word=tmp[0]
# mean=' '.join(tmp[1:]).strip()
# print(word)
# print(mean)

sql="insert into words (word,unpuzzle) values (%s,%s)"

for line in  f:
    # 获取单词和解释
    tup=re.findall(r"(\S+)\s+(.*)",line)[0]
    try:
        cur.execute(sql,tup)
        db.commit()
    except:
        db.rollback()

# 关闭数据库
cur.close()
db.close()

