from flask import Flask, request, jsonify, render_template
import sqlite3
import gmpy2

app = Flask(__name__)

DATABASE = 'pi_digits.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS pi (digits INTEGER PRIMARY KEY, value TEXT)')
    conn.commit()
    conn.close()

def get_pi(digits):
    precision_bits = int(digits * 3.32192809489)
    gmpy2.get_context().precision = precision_bits
    return str(gmpy2.const_pi())[:digits + 2]

def store_pi_in_db(digits, value):
    conn = get_db_connection()
    conn.execute('INSERT OR IGNORE INTO pi (digits, value) VALUES (?, ?)', (digits, value))
    conn.commit()
    conn.close()

def get_pi_from_db(closest_digits):
    conn = get_db_connection()
    pi_row = conn.execute('SELECT value FROM pi WHERE digits = ?', (closest_digits,)).fetchone()
    conn.close()
    if pi_row:
        return pi_row['value']
    return None

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/calculate-pi', methods=['POST'])
def calculate_pi():
    digits = request.json.get('digits', 100)

    # Check if requested digits exceed the limit of 10 million
    if digits > 10000000:
        return jsonify({'error': 'Cannot compute more than 10 million digits of Pi.'}), 400

    digits = min(digits, 1000000)  # Limit to 1 million digits

    # Fetch the closest higher interval of digits stored in the database
    closest_digits = ((digits - 1) // 10000 + 1) * 10000
    pi_str = get_pi_from_db(closest_digits)

    if pi_str:
        # Return only the requested number of digits
        pi_str = pi_str[:digits + 2]
    else:
        # If not found, calculate it, store it, and then return it
        pi_str = get_pi(digits)
        store_pi_in_db(closest_digits, pi_str)

    return jsonify({'pi': pi_str})

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
