from app import app, db
from flask import render_template, redirect, url_for, flash
from app.forms import PhoneNumberForm
from app.models import User

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
        phone_number  = form.phone_number.data 
        check_number = db.session.execute(db.select(User).filter(User.phone_number == phone_number)).scalars().all()
        if check_number:
            flash('Phone Number already exists🥲!')
            return redirect(url_for('phone_number'))
        new_user = User(first_name=first_name, last_name=last_name, address=address, phone_number=phone_number)
        flash(f"Success😁 Phone number {phone_number} has been added to the Phone Book!")
        return redirect(url_for('index'))
    return render_template('phone_number.html', form=form)
