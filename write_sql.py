"""
写操作 (insert update delete)
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

# 写数据库
try:
    # 写sql语句执行

    # # 插入操作
    # name=input('Name:')
    # age=input('Age:')
    # score =input('Score:')
    #
    # # 将变量插入到sql语句合成最终操作语句
    # sql="insert into class (name,age,score) values (%s,%s,%s)"
    # # 可以使用列表直接给sql语句的values传值
    # cur.execute(sql,[name,age,score])#执行

    # # 修改操作
    # sql="update interest set price=11800 where name ='baron';"
    # cur.execute(sql)

    # # 删除操作
    # sql="delete from class where score<90"
    # cur.execute(sql)

    db.commit() # 提交

except Exception as e:
    # 退回到commit执行之前的数据库状态
    db.rollback()
    print(e)

# 关闭数据库
cur.close()
db.close()

