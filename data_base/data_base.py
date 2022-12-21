import mariadb
import sys

class Data_base:
    def __init__(self):
        try:
            conn = mariadb.connect(user='root', password='saulh970625', host='192.0.2.1', port=3306, database="negocio")
        except mariadb.Error as e:
            print(f'Error connecting to MriaDB Platform: {e}')

        cur = conn.cursor()