import pymysql.cursors


def process_mysql(client_data):
    connection = pymysql.connect(host='localhost',
                                 user='test_app_user',
                                 password='********',
                                 db='test_app',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor
                                 )
    try:
        with connection.cursor() as cursor:
            sql = 'INSERT INTO tbl (name, age, city) VALUES (%s, %s, %s)'
            cursor.execute(sql, (client_data['name'], client_data['age'], client_data['city']))
        connection.commit()
    finally:
        connection.close()
