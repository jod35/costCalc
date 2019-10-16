from cost import app,db
from flask import render_template,request,redirect,url_for,flash
from cost.forms import CostForm
from cost.models import Calculation

@app.route('/calculate',methods=['POST'])
def calc():
   form=CostForm()
   cost_price=form.cost_price.data
   mark_up=form.mark_up.data
   discount=form.discount.data
   
   profit=((mark_up/100) * cost_price)

   selling_price = ((cost_price + profit) - (cost_price * (discount/100)))

   new_calc=Calculation(cost_price=cost_price,discount=discount,mark_up=mark_up,selling_price=selling_price)

   db.session.add(new_calc)
   db.session.commit()
   flash("The new selling price is UGX%s"%selling_price)
   return redirect(url_for('index'))

@app.route('/')
def index():
   calculations=Calculation.query.all()
   form=CostForm()
   return render_template("index.html",form=form,calculations=calculations)


   