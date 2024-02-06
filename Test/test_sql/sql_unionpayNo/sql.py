import pymysql

from Test.yaml_util import read_yaml

db = pymysql.connect(
    host='192.168.20.10',
    port=3369,
    user='root',
    password='123',
    database='drbt_centralizer_app_kernel',
    charset='utf8mb4'
)
# 执行sql方法
# print(read_yaml('sql'))
cursor = db.cursor()
# 租户id
tenant = [100000000000000001, 334944430295367680, 123480379607748607, 334893626456817664]
# {100000000000000001 : '河南vivo', 334944430295367680 : '河南电教', 123480379607748607 : '河南OPPO', 334893626456817664 : '鼓点测试'}
# cursor.execute(read_yaml('id'))
# resul = cursor.fetchall()
# db.commit()
i = 166253778213871425
# 获取sql
sql_list = read_yaml('sql').split(";")
del sql_list[-1]
# 循环插入
for j in tenant:
    for sql_t in sql_list:
        sql = sql_t.replace('{ID}', str(i)).replace('{tenant_id}', str(j))
        print(sql)
        cursor.execute(sql)
        db.commit()
        print('导入成功')
        i = i + 1
        
        # print(sql_t)
# 关闭数据库
db.close()
print('已关闭数据库连接')