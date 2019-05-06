import mysql.connector
mydb = mysql.connector.connect(
  host="rimsdev.mysql.pythonanywhere-services.com",
  user="rimsdev",
  passwd="rimsventory"
)

mycursor = mydb.cursor()

mycursor.execute("USE rimsdev$inventory")

searchuser = "SELECT firstname, lastname FROM users"

mycursor.execute(searchuser)

res = mycursor.fetchall()

for x in res:
  print(x)
