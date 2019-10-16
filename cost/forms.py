from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class CostForm(FlaskForm):
    cost_price=IntegerField("Cost Price")
    mark_up=IntegerField("Mark Up")
    discount=IntegerField("Discount")
    update=SubmitField("CalculateThe Price")
    