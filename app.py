from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def top():
    return render_template("index.html")

@app.route("/a")
def a():
    return render_template("a.html")

@app.route("/a2")
def a2():
    pay = request.args.get("pay")
    hours = request.args.get("hours")
    pay = int(pay)
    hours = int(hours)
    money = salary(pay, hours)
    return render_template("a2.html", money=money)

def salary(pay, hours):
    money = pay * hours
    return money

@app.route("/b")
def b():
    return render_template("b.html")

@app.route("/b2")
def b2():
    radius = request.args.get("radius")
    radius = int(radius)
    menseki = round(radius)
    return render_template("b2.html", menseki=menseki)

def round(radius):
    menseki = radius * radius * 3.14
    return menseki

if __name__=="__main__":
    app.run(debug=True)
