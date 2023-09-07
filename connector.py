import mysql.connector
import pandas, json
import random
# ________ MySQL Connector_____
class MySQL():
    def __init__(self):
        self.mydb = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                passwd = '123456789',
                database = 'vocabularydb'
            )
        self.mycursor = self.mydb.cursor()
    # Return Value As Tuple
    def get_data(self):
        self.mycursor.execute('SELECT * FROM vocabulary')
        my_result = self.mycursor.fetchall()
        return my_result
    def data_condition(self,fromNum,toNum):
        self.mycursor.execute(f'SELECT * FROM vocabulary WHERE id BETWEEN {fromNum} AND {toNum}')
        my_result = self.mycursor.fetchall()
        return my_result    
    def add(self,eng,viet):
        sql = "INSERT INTO vocabulary (english,vietnamses) VALUES (%s,%s)"
        val = (eng,viet)
        self.mycursor.execute(sql,val)
        self.mydb.commit()
    def delete(self,id):
        sql = f"DELETE FROM vocabulary WHERE id = {id}"
        self.mycursor.execute(sql)
        self.mydb.commit()
    def reset_id(self):
        # Tắt AUTO_INCREMENT
        self.mycursor.execute('ALTER TABLE vocabulary MODIFY COLUMN id INT')
        # Cập nhật lại giá trị ID
        self.mycursor.execute('SET @new_id := 0')
        self.mycursor.execute('UPDATE vocabulary SET id = (@new_id := @new_id + 1) ORDER BY id')
        # Bật lại AUTO_INCREMENT
        self.mycursor.execute('ALTER TABLE vocabulary MODIFY COLUMN id INT AUTO_INCREMENT')
        self.mydb.commit()
    def edit(self,id,viet_edit):
        self.mycursor.execute(f"UPDATE vocabulary SET vietnamses = {viet_edit} WHERE id = {id}")
        self.mydb.commit()
# import mysql.connector

# mydb = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     passwd='123456789',
#     database='vocabularydb'
# )

# mycursor = mydb.cursor()

# # Sắp xếp dữ liệu theo ID
# mycursor.execute('SELECT * FROM vocabulary ORDER BY id')
# data = mycursor.fetchall()

# # Cập nhật lại trường ID
# new_id = 1
# for row in data:
#     sql = f"UPDATE vocabulary SET id = {new_id} WHERE id = {row[2]}"
#     mycursor.execute(sql)
#     new_id += 1

# mydb.commit()
    # def upgrade(self,id)
# mydb = mysql.connector.connect(
#                 host = 'localhost',
#                 user = 'root',
#                 passwd = '123456789',
#                 database = 'vocabularydb'
#             )
# mycursor = mydb.cursor()
# mycursor.execute(f'SELECT * FROM vocabulary WHERE id BETWEEN {235} AND {240} ')
# myresult = mycursor.fetchall()

# random.shuffle(myresult)
# print(random.choice(myresult))




# mydb = MySQL()
# myresult = mydb.add('global boiling','sự nóng lên toàn cầu')
# print(myresult)
# random.shuffle(myresult)
# print(type(myresult))

# x = random.choice(myresult)

# eng = x[0]
# viet = x[1]
# print(eng)
# print(viet)




# 
# num1 = input()
# num2 = input()
# mycursor.execute(f'SELECT * FROM vocabulary WHERE id BETWEEN {num1} AND {num2}')

# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)



# data = pandas.read_csv('data.csv')
# get data in row
# to_learn = data.to_dict(orient='records')


#____________GET DATA________
# all_words = []

# tuple_list = []

# for num in range(len(to_learn)):
#     tuple_list = (to_learn[num]['English'], to_learn[num]['Tiếng Việt'])
#     all_words.append(tuple_list)




# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]
# print(type(val[1]))



#____________CREATing DATA_______

# mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")

# _________Creating a Table_________

# mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

#_________ Insert Into Table________

# sql = 'INSERT INTO vocabulary(english,vietnamses) VALUES(%s,%s)'
# mycursor.executemany(sql,all_words)
# mydb.commit()
# print(mycursor.rowcount, "was inserted.")