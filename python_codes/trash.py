def log_in(self):
        try:
            self.db.query_sql(comand='SELECT user FROM users')
            for user in self.db.cur:
                print(type(self.db.cur))
                if  str("('"+self.user_entry.get()+"',)") == str(user):
                    print('Usuario correcto')
                    break
                else:
                    print('Usuario incorrecto')
        except mariadb.Error as e:
            print(f'Error {e}')

            self.db.query_sql(comand='SELECT count(*) FROM users')
            for num_user in self.db.cur:
                users = num_user[0]
                print(type(users))