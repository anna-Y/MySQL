"""
pymysql二进制图片存储
"""

import pymysql

# 连接数据库
db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                   password='123456',
                   database='student1',
                   charset='utf8')

# 获取游标（操作数据库，执行sql语句）
cur=db.cursor()

# # 存储图片---图片过大
# with open('cyb.jpg','rb') as f:
#     data=f.read()
# try:
#     sql="update class set image = %s where name='Jame';"
#     cur.execute(sql,[data])
#     db.commit()
# except Exception as e:
#     db.rollback()
#     print(e)

# 获取图片
sql = "select * from class where name = 'Jame'"
cur.execute(sql)
data=cur.fetchone()     # 元组
with open('zhenghj.jpg','wb') as f:
    f.write(data[6])        #提取，对应索引号

# 关闭数据库
cur.close()
db.close()

