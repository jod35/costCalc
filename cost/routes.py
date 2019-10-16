from cost import app,db
from flask import render_template
from cost.forms import CostForm

@app.route('/')
def index():
   return render_template("index.html")