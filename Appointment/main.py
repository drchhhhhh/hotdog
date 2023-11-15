from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TimeField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SECRET_KEY'] = 'secret_key'  # Change this to a secure secret key
db = SQLAlchemy(app)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.String(10), nullable=False)

class AppointmentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    time = TimeField('Time', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/')
def index():
    appointments = Appointment.query.all()
    return render_template('index.html', appointments=appointments)

@app.route('/add_appointment', methods=['GET', 'POST'])
def add_appointment():
    form = AppointmentForm()

    if form.validate_on_submit():
        appointment = Appointment(
            name=form.name.data,
            email=form.email.data,
            date=form.date.data,
            time=form.time.data
        )
        db.session.add(appointment)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('add_appointment.html', form=form)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
