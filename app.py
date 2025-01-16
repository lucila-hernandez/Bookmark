from flask import Flask, render_template, request
import os
import requests
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
API_KEY = os.getenv('API_KEY')
API_URL = 'https://www.googleapis.com/books/v1/volumes'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    params = {'q': query, 'key': API_KEY}
    response = requests.get(API_URL, params=params)

    print(f"Status Code: {response.status_code}")
    print(f"Response Content: {response.content}")

    if response.status_code == 200:
        try:
            books = response.json().get('items', [])
        except requests.exceptions.JSONDecodeError as e:
            print(f"JSONDecodeError: {e}")
            books = []
    else:
        books = []

    return render_template('search_results.html', books=books)

if __name__ == '__main__':
    app.run(debug=True, port=5000)