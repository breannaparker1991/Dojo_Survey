from flask import Flask, session
from flask_app.gitignore.env import KEY

app = Flask(__name__)
app.secret_key = KEY
