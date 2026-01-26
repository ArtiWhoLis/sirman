import mysql.connector
from mysql.connector import Error

class DBConnection:
    def __init__(self):
        self.host='localhost'  # адрес из Open Server
        self.user='artiwho'  # пользователь
        self.password='pyzloh123'  # пароль
        self.database='schooldb' 
        self.connection = None
        self.cursor = None
#метод на открытие
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database

            )
            self.cursor = self.connection.cursor(dictionary=True)
            print("База данных подключена")
            return True

        except Error as e:
            print(f"Ошибка подключения: {e}")
            return False
#метод на закрытие
    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("База данных отключена")

    def get_all_tables(self):
        try:
            self.cursor.execute('SHOW TABLES')
            tables = self.cursor.fetchall()
            for t in tables:
                print(t['Tables_in_schooldb'])

            return True

        except Error as e:
            print(f"Ошибка выполнения запроса: {e}")
            return False
        
    def execute_query(self,query):
        try:
            self.cursor.execute(query)
            query_type = query.strip().upper().split()[0] #удаляет все ненужные строки, капс, разделяет по пробелам

            if query_type == 'SELECT' or 'DESCRIBE':
                return self.cursor.fetchall()
            else:
                self.connection.commit() #необходим для выполнения запроса
                return self.cursor.rowcount # необходим для возвращения результата
        except Error as e:
            print(f"Ошибка выполнения запроса: {e}")
            return True

        
    def get_table_info(self, table_name):
        return self.execute_query(f'DESCRIBE {table_name}')
    
    def get_all_person(self):
        query = 'SELECT * FROM person'
        return self.execute_query(query)
    
    def __enter__(self):
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()
