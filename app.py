from flask import Flask, render_template
import os

app = Flask(__name__)

API_KEY = os.getenv('API_KEY')

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)