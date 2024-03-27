from flask import Flask, render_template, request, redirect, flash, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, URL, Email
from flask_ckeditor import CKEditor, CKEditorField
import os

# Create Flask application
app = Flask(__name__)
# TODO Confirm need for csrf protection
# Add csrf protection
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')
# Initialise Bootstrap-Flask
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe_name = StringField('Cafe name', validators=[DataRequired()])
    cafe_location = StringField("Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()])
    coffee_rating = SelectField("Coffee Rating", choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])
    wifi_rating = SelectField("Wifi Strength Rating", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    power_rating = SelectField("Power Socket Availability", choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    submit = SubmitField('Submit')


# TODO update both url_for links in index.html
@app.route("/")
def home():
    return render_template("index.html")


# TODO Edit the form UI on the add new cafe page
@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('add.html', form=form)

# TODO Create edit cafe page

# TODO Add user account login
# TODO Consider Google login
# TODO Create cafe listings database (name, location, coffee, wifi, power, seats, user_id)
# TODO Create user database (user email, password, name)
# TODO Create API to call data from database to website


if __name__ == '__main__':
    app.run(debug=True, port=5002)

