from flask import Flask

app = Flask(__name__)

# Load configuration
app.config.from_object('config')

from app import routes

