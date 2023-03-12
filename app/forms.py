from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, DecimalField, FileField
from wtforms.validators import DataRequired, NumberRange, InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()])
    description = TextAreaField('Property Description', validators=[InputRequired()],render_kw={"rows": 8, "cols": 70})
    rooms = IntegerField('No. of Rooms', validators=[InputRequired(), NumberRange(min=1, max=10)])
    bathrooms = IntegerField('No. of Bathrooms', validators=[InputRequired(), NumberRange(min=1, max=5)])
    price = DecimalField('Price', validators=[InputRequired()])
    property_type = SelectField('Property Type', choices=[('apartment', 'Apartment'), ('house', 'House'), ('condo', 'Condo')])
    location = StringField('Location', validators=[InputRequired()])
    photo=FileField('Photo', validators=[FileRequired(),FileAllowed(['jpg', 'png','jpeg'], 'Images only!')])

