import mariadb
import sys

class Data_base:
    def __init__(self):
        try:
            self.conn = mariadb.connect(user='root', password='saulh970625', port=3306, database="PDV")
            print('Conexion exitosa')
        except mariadb.Error as e:
            print(f'Error connecting to MariaDB Platform: {e}')

    def query_sql(self, command):
        try:
            self.cur = self.conn.cursor()
            aux = self.cur.execute(command)
            return aux
        except mariadb.Error as e:
            print(f'Error {e}')

    def delete_sql(self, command):
        try:
            self.cur = self.conn.cursor()
            self.cur.execute(command)
        except mariadb.Error as e:
            print(f'Error {e}')

    def modify_sql(self,command):
        try:
            self.cur = self.conn.cursor()
            self.cur.execute(command)
            self.conn.commit()
        except mariadb.Error as e:
            print(f'Error {e}')

    def insert_sql(self,command):
        try:
            self.cur = self.conn.cursor()
            self.cur.execute(command)
        except mariadb.Error as e:
            print(f'Error {e}')

    def close_sql(self):
        self.conn.close()

if __name__ == '__main__':
    db = Data_base()
    db.query_sql()