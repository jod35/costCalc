from cost import app,db
from flask import render_template
from cost.forms import CostForm

@app.route('/')
def index():
   form=CostForm()
   return render_template("index.html",form=form)