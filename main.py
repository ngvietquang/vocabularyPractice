from flask import Flask, render_template,url_for
from connector import MySQL
import random
app = Flask(__name__)
mydb = MySQL()

@app.route('/')
def home():
    all_vocabulary = mydb.get_data()
    vocabulary = random.choice(all_vocabulary)
    current_english_word = vocabulary[0]
    current_vietnam_word = vocabulary[1]
    return render_template('index.html',

                           current_english_word = current_english_word,
                           current_vietnam_word = current_vietnam_word)

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/revision')
def revision():
    return render_template('counter.html')
if __name__ == '__main__':
    app.run(debug=True)