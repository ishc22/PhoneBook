from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import PhoneNumberForm

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/phone_number", methods=['GET', 'POST'])
def phone_number():
    form = PhoneNumberForm()
    if form.validate_on_submit():
        first_name = form.first_name.data 
        last_name = form.last_name.data 
        address = form.address.data 
        phone_number  = form.phone_number .data 
        flash("Success!!!Phone number has been added to the Phone Book.")
        return redirect(url_for('index'))
    return render_template('phone_number.html', form=form)
