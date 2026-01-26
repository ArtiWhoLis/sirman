from config.database import DBConnection
from mysql.connector import Error

db = DBConnection()
with db:
   print("\nСтруктура таблицы 'person'")
   for field in db.get_table_info('person'):
      print(f" - {field['Field']}: {field['Type']}")
   print("\nДанные в таблице 'person'")
   for person in db.get_all_person():
      print(f"{person['FirstName']}  {person['LastName']}, email: {person['Email']}")
   
 