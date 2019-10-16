from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField

class CostForm(FlaskForm):
    cost_price=IntegerField("Cost Price")
    Mark_Up=IntegerField("Mark Up")
    