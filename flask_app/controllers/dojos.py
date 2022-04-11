from flask import Flask, render_template, session, request, redirect
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def first():
  return render_template("index.html")

@app.route('/main', methods=["POST"])
def main():
  if Dojo.validate(request.form):
    Dojo.create(request.form)
  # session['name'] = request.form['name']
  # session['location'] = request.form['location']
  # session['langauge'] = request.form['language']
  # session['comment'] = request.form['comment']
    return redirect ('/results')
  return redirect('/')

@app.route('/results')
def results():
  return render_template("submit.html", name=session['name'], 
  location=session['location'], language=session['langauge'],
  comment=session['comment'])