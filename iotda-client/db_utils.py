import pymysql
import pojos

HOST = "localhost"
USER = "root"
PWD = "123456"
DATABASE = "wlwdata"


def connMySql():
    return pymysql.connect(host=HOST, user=USER, password=PWD, database=DATABASE)


# 开始事务
def exeSql(sql, params):
    d = connMySql()
    c = d.cursor()
    try:
        c.execute(sql, params)
        d.commit()
    except Exception as e:
        print(e)
        d.rollback()
    finally:
        c.close()
        d.close()


def insert_cover(data: pojos.Cover):
    sql = "insert into covers (temp, accel_x, accel_y, accel_z, cover_status,date, name, sno) values(%s, %s, %s, %s, %s, %s, %s, %s)"
    exeSql(sql, tuple(data))


def insert_smoke(data: pojos.Smoke):
    sql = "insert into smokes (smoke_value, beep_status, date, sno, name) values(%s, %s, %s, %s, %s)"
    exeSql(sql, tuple(data))
