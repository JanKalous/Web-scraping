import pandas as pd
import sqlite3 as sql
df = pd.read_csv(r'C:\Users\hkalo\naucse-python\Foxconn\datafox.csv')
print(df)
conn = sql.connect('fox.db')
df.to_sql('Jan_Kalous', conn)
datakal = pd.read_sql('SELECT Region,Rep,Item,Units,FinalDiscount,FinalPrice,CreationDate,OrderDate FROM Jan_Kalous', conn)
print(datakal)
datakal.to_csv('finaldata.csv', index=False)