import pymysql

from yaml_util import read_yaml

db = pymysql.connect(
    host='192.168.20.10',
    port=3369,
    user='root',
    password='123',
    database='drbt_centralizer_app_kernel',
    charset='utf8mb4'
)
# 执行sql方法
print(read_yaml('id'))
cursor = db.cursor()
# 获取最新的id
cursor.execute(read_yaml('id'))
resul = cursor.fetchall()
db.commit()
i = resul[0][0] + 1
# 获取sql
sql_list = read_yaml('emp').split(";")
del sql_list[-1]
# 循环插入
for sql_t in sql_list:
    sql = sql_t.replace('{id}', str(i))
    cursor.execute(sql)
    db.commit()
    print('导入成功')
    i = i + 1
    # print(sql_t)
# 关闭数据库
db.close()
print('已关闭数据库连接')
