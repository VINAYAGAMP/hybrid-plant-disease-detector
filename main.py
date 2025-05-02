# main.py
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable cross-origin requests

@app.route('/')
def home():
    return "ExpenseStreamline Backend Running!"

@app.route('/add-expense', methods=['POST'])
def add_expense():
    data = request.json
    # Here you would handle storing expenses
    return jsonify({"message": "Expense added", "data": data})

if __name__ == '__main__':
    app.run()
