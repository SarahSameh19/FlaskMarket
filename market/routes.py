from market import app
from flask import render_template, redirect, url_for
from market.models import Item, User
from market.forms import RegisterForm
from market import db
from flask import request  # Make sure to import request

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

@app.route('/register', methods=['GET','POST'])
def register_page():
    form = RegisterForm()
        
    if form.validate_on_submit():
        print(f"Username Field Data from Form: {form.username.data}")  # What Flask-WTF sees
        user_to_create = User(
                            username= form.username.data,
                            email_address=form.email_address.data,
                            password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))  
    if form.errors != {}: #if there are not errors from the validations
        for err_msg in form.errors.values():
            print(f'there was an error with creating a user: {err_msg}') #print error message

    return render_template('register.html', form=form)