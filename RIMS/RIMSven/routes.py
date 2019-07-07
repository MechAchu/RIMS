from flask import Flask, render_template, render_template, url_for, flash, redirect
from RIMSven import app, db, bcrypt
from RIMSven.models import Users, Tools, Consumables
from RIMSven.forms import Registration, Login

UsErS = {
    'person': 'Jacob',
    'table': 'Users',
    'content': 'List of people in robotics'
    }

ItEmS = {
    'person': 'Jacob',
    'table': 'Items',
    'content': 'List of items'
    }

CoNsUmAbLeS = {
    'person': 'Jacob',
    'table': 'Consumables',
    'content': 'List of consumables'
    }

data = [UsErS, ItEmS, CoNsUmAbLeS]

@app.route("/")
def home():
    return render_template('Home Page.html', data=data)

@app.route("/database")
def database():
    return render_template('Database_Page.html', data=data)

@app.route("/UserDatabase")
def UserDatabase():
    return render_template('UserDatabase_Page.html', data=data)

@app.route("/ToolsDatabase")
def ItemsDatabase():
    return render_template('ItemsDatabase_Page.html', data=data)

@app.route("/ConsumablesDatabase")
def ConsumablesDatabase():
    return render_template('ConsumablesDatabase_Page.html', data=data)



@app.route("/register", methods=['GET', 'POST'])
def register():
    form = Registration()
    if(form.validate_on_submit()):
        hashed_ID = bcrypt.generate_password_hash(form.ID.data).decode('utf-8')
        user = Users(first_name=form.first_name.data, last_name=form.last_name.data, ID=hashed_ID)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.first_name.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = Login()
    if(form.validate_on_submit()):
        if(form.email.data == 'admin@blog.com' and form.password.data == 'password'):
            flash('Logged In!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please Try Again.', 'danger')
    return render_template('login.html', title='Login', form=form)
