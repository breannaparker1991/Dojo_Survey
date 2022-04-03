from env import KEY
from flask import Flask, render_template, session, request, redirect
from env import KEY

app = Flask(__name__)
app.secret_key = KEY

@app.route('/')
def main():
  return render_template("index.html")

# @app.route('/result' method=["POST"])

if __name__ == "__main__":
  app.run(debug=True)

