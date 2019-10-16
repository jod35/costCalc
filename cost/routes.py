from cost import app,db
from flask import render_template,request,redirect,url_for
from cost.forms import CostForm

previous_calculations=[

]
@app.route('/')
def index():
   form=CostForm()
   return render_template("index.html",form=form)

@app.route('/calculate')
def calculate():
   return redirect(url_for('index'))