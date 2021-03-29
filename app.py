from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def top():
    return render_template("inde.html")

@app.route("/a")
def a():
    return render_template("a.html")

@app.route("/b")
def b():
    return render_template("b.html")

if __name__=="__main__":
    app.run(debug=True)