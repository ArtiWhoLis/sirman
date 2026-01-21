import mysql.connector

try:
    db = mysql.connector.connect(
        host='localhost',  # адрес из Open Server
        user='Anna',  # пользователь
        password='r0st0v',  # пароль
        database='final'  # название базы
    )

    print("База данных подключена")

    cursor = db.cursor()

    print("Таблицы в базе 'final':")
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()

    if tables:
        for table in tables:
            print(table[0])
    else:
        print("В базе нет таблиц")

    if ('person',) in tables:
        print("Содержимое таблицы 'person':")
        cursor.execute("SELECT * FROM person")
        persons = cursor.fetchall()

        if persons:
            for person in persons:
                print(f"   - ID: {person[0]}, Телефон: '{person[1]}', ФИО: {person[2]}")
        else:
            print("Таблица 'person' пуста")

        print("Структура таблицы 'person':")
        cursor.execute("DESCRIBE person")
        columns = cursor.fetchall()
        for column in columns:
            print(f"   • {column[0]} - {column[1]} ({'NULL' if column[2] == 'YES' else 'NOT NULL'})")
    else:
        print("Таблицы 'person' не существует!")
        
    if ('buildings',) in tables:
        print("Содержимое таблицы 'buildings':")
        cursor.execute("SELECT * FROM buildings")
        buildings = cursor.fetchall()

        if buildings:
            for building in buildings:
                print(f"   - ID: {building[0]}, Телефон: '{building[1]}', ФИО: {building[2]}")
        else:
            print("Таблица 'buildings' пуста")

        print("Структура таблицы 'buildings':")
        cursor.execute("DESCRIBE person")
        columns = cursor.fetchall()
        for column in columns:
            print(f"   • {column[0]} - {column[1]} ({'NULL' if column[2] == 'YES' else 'NOT NULL'})")
        else:
        	print("Таблицы 'buildings' не существует!")
    
	cursor.close()
    db.close()
    print("Соединение закрыто")

except mysql.connector.Error as e:
    print(f"ОШИБКА ПОДКЛЮЧЕНИЯ: {e}")
    

	