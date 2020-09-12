import pyodbc
import pandas as pd

def read(connection):
  print("Read")
  cursor = connection.cursor()
  cursor.execute('''\
  SELECT cast([time] as date) time
      ,[shift]
      ,[shovel_operator_last_name]
      ,[shovel_operator_first_name]
      ,[shovel]
      ,[shovel_equipment_type]
      ,[load_count]
      ,[material_tonnage]
      ,[payload]
      ,[payload_count]
	  ,(payload/nullif(payload_count,0)) as avg_payload
  FROM [jmineops].[dbo].[by_shovel_operator_loads]
  where deleted_at is null and shovel_operator is not null
  ''')
  for row in cursor:
    print(row)
  print()

connection = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=192.168.200.31;"
    "Database=jmineops;"
    "Trusted_Connection=yes;"
)

shovel_op_loads = read(connection)

shovel_op_loads.head()