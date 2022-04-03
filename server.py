from flask import Flask, render_template
app = Flask(__name__)
app.secret_key = "the key is a secret, the secret is the key"

@app.route('/')
def main():
  return render_template("index.html")

# @app.route('/result' method=["POST"])

if __name__ == "__main__":
  app.run(debug=True)

