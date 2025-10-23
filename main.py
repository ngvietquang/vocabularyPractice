from flask import Flask, render_template,flash, url_for, redirect
from connector import MySQL
from flask_wtf import FlaskForm
from wtforms import StringField , SubmitField , IntegerField
from wtforms.validators import DataRequired
import random
app = Flask(__name__)
mydb = MySQL()
app.config['SECRET_KEY'] = 'aD1Cas'

class FormEdit(FlaskForm):
    viet_edit = StringField(validators=[DataRequired()])
    submit_edit = SubmitField(label='Submit',validators=[DataRequired()])
class FormCount(FlaskForm):
    fromNum = IntegerField(validators=[DataRequired()])
    toNum = IntegerField(validators=[DataRequired()])
    submit = SubmitField(label='Submit',validators=[DataRequired()])
class FormAdd(FlaskForm):
    eng = StringField(validators=[DataRequired()]) 
    viet = StringField(validators=[DataRequired()])
    submit = SubmitField(label='Submit',validators=[DataRequired()])


@app.route('/',methods = ['POST','GET'])
def home():
    all_vocabulary = mydb.get_data()
    random.shuffle(all_vocabulary)
    return render_template('index.html',
                            all_vocabulary =all_vocabulary,
                            )                      

@app.route('/add',methods=['GET','POST'])
def add():
    form = FormAdd()
    if form.validate_on_submit():
        eng = form.eng.data.lower()
        viet = form.viet.data.lower()
        form.eng.data =''
        form.viet.data=''
        print(form.errors)
        mydb.add(eng=eng,viet=viet)
        flash('Vocabulary Added Successfully!!')
        return render_template('add.html',
                           form=form)
    return render_template('add.html',
                           form=form)

@app.route('/revision',methods=['GET','POST'])
def revision():

    formCount = FormCount()
    if formCount.validate_on_submit():
        fromNum = formCount.fromNum.data
        toNum = formCount.toNum.data
        formCount.fromNum.data=''
        formCount.toNum.data =''
        all_vocabulary = mydb.data_condition(fromNum=fromNum,toNum=toNum)
        return render_template('index.html',
                            all_vocabulary =all_vocabulary,
                            )  
    return render_template('counter.html',
                           formCount = formCount)
@app.route('/vocabulary-data',methods = ['GET','POST'])
def vocabulary_data():
    all_vocabulary = mydb.get_data()
    return render_template('show_data.html',
                           all_vocabulary = all_vocabulary)
@app.route('/delete/<int:id>', methods = ['GET','POST'])
def delete(id):
    mydb.delete(id)
    mydb.reset_id()
    flash("Vocabulary Deleted Successfully!!")
    all_vocabulary = mydb.get_data()
    return render_template('show_data.html',
                           all_vocabulary = all_vocabulary)
@app.route('/edit/<int:id>', methods = ['GET','POST'])
def edit(id):
    current_id = id
    form = FormEdit()
    if form.validate_on_submit():
        viet_edit = form.viet_edit.data
        form.viet_edit.data =''
        mydb.edit(current_id,viet_edit)
        return redirect(url_for('vocabulary_data()'))
    return render_template('edit.html',
                           form = form)

if __name__ == '__main__':
    app.run(debug=True)