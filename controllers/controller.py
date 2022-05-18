from flask import render_template
from app import app
from models.order_list import orders


@app.route("/")
def index():
    return "Hello World!"


@app.route("/orders")
def get_orders():
    return render_template("index.html", title="Home Page", orders=orders)
