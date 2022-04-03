from flask import Flask, render_template, session, request, redirect
from env import KEY

app = Flask(__name__)
app.secret_key = KEY

@app.route('/')
def first():
  return render_template("index.html")

@app.route('/main', methods=["POST"])
def main():
  session['name'] = request.form['name']
  session['location'] = request.form['location']
  session['langauge'] = request.form['language']
  session['comment'] = request.form['comment']
  return redirect ('/results')

@app.route('/results')
def results():
  return render_template("submit.html", name=session['name'], 
  location=session['location'], language=session['langauge'],
  comment=session['comment'])

if __name__ == "__main__":
  app.run(debug=True)

