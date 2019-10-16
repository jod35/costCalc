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
   profit=(cost_price*(mark_up/100))
   s_price=cost_price + profit
   disc=(discount/100) * s_price 
   selling_price=s_price -disc
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


@app.route('/delete/<int:id>')
def delete(id):
   calculation_to_be_deleted=Calculation.query.get_or_404(id)
   db.session.delete(calculation_to_be_deleted)
   db.session.commit()
   return redirect('index')