import mysql.connector
import pandas, json
import random
# data = pandas.read_csv('data.csv')
# get data in row
# to_learn = data.to_dict(orient='records')


#____________GET DATA________
# all_words = []

# tuple_list = []

# for num in range(len(to_learn)):
#     tuple_list = (to_learn[num]['English'], to_learn[num]['Tiếng Việt'])
#     all_words.append(tuple_list)

#________ MySQL Connector_____

    
    


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
        self.mycursor.execute('SELECT english,vietnamses FROM vocabulary')
        my_result = self.mycursor.fetchall()
        random.shuffle(my_result)
        return my_result
    def max_id(self):
        self.mycursor.execute(f'SELECT id FROM vocabulary ORDER BY id DESC')
        my_result = int(self.mycursor.fetchone()[0])
        return my_result


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
# myresult = mydb.get_data()
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