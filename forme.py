from wtforms import SubmitField, DecimalField, IntegerField
from wtforms.validators import NumberRange, InputRequired
from flask_wtf import FlaskForm


class Zad1Form(FlaskForm):
    xmin = DecimalField('xmin', validators=[InputRequired('Obavezan unos minimuma na x osi!'), NumberRange(min=0,message='Minimum je 0!')])
    xmax = DecimalField('xmax', validators=[InputRequired('Obavezan unos maksimuma na x osi!'), NumberRange(min=1,message='Minimum je 1!')])

    a1 = DecimalField('a', validators=[InputRequired()])
    b1 = DecimalField('b', validators=[InputRequired()])
    c1 = DecimalField('c', validators=[InputRequired()])

    a2 = DecimalField('a', validators=[InputRequired()])
    b2 = DecimalField('b', validators=[InputRequired()])
    c2 = DecimalField('c', validators=[InputRequired()])
    nacrtaj = SubmitField('Nacrtaj')

class Zad2Form(FlaskForm):
    inpMinR = IntegerField('inpMinR', validators=[InputRequired(), NumberRange(min=0, max=255, message='0-255!')])
    inpMaxR = IntegerField('inpMaxR', validators=[InputRequired(), NumberRange(min=0, max=255, message='0-255!')])
    outMinR = IntegerField('outMinR', validators=[InputRequired(), NumberRange(min=0, max=255, message='0-255!')])
    outMaxR = IntegerField('outMaxR', validators=[InputRequired(), NumberRange(min=0, max=255, message='0-255!')])

    inpMinG = IntegerField('inpMinG', validators=[InputRequired(), NumberRange(min=0, max=255, message='0-255!')])
    inpMaxG = IntegerField('inpMaxG', validators=[InputRequired(), NumberRange(min=0, max=255, message='0-255!')])
    outMinG = IntegerField('outMinG', validators=[InputRequired(), NumberRange(min=0, max=255, message='0-255!')])
    outMaxG = IntegerField('outMaxG', validators=[InputRequired(), NumberRange(min=0, max=255, message='0-255!')])

    inpMinB = IntegerField('inpMinB', validators=[InputRequired(), NumberRange(min=0, max=255, message='0-255!')])
    inpMaxB = IntegerField('inpMaxB', validators=[InputRequired(), NumberRange(min=0, max=255, message='0-255!')])
    outMinB = IntegerField('outMinB', validators=[InputRequired(), NumberRange(min=0, max=255, message='0-255!')])
    outMaxB = IntegerField('outMaxB', validators=[InputRequired(), NumberRange(min=0, max=255, message='0-255!')])

    nacrtaj = SubmitField('Prikazi normalizovanu sliku')
