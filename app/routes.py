from flask import render_template
from app import app

# Route untuk halaman utama
@app.route('/')
def index():
    return render_template('index.html')

# Route untuk halaman about
@app.route('/about')
def about():
    return render_template('about.html')
