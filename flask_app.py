from flask import Flask, render_template, jsonify
import requests
import sqlite3
import time
from datetime import datetime

app = Flask(__name__)

# Initialisation de la base de données
def init_db():
    conn = sqlite3.connect('tests.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS test_runs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        name TEXT,
        status_code INTEGER,
        response_time REAL,
        age INTEGER,
        count INTEGER,
        success INTEGER
    )''')
    conn.commit()
    conn.close()

init_db()

@app.get("/")
def consignes():
    return render_template('consignes.html')

@app.get("/run-tests")
def run_tests():
    names = ["michael", "hamedy", "alice", "bob", "camara"]
    results = []

    for name in names:
        start = time.time()
        try:
            response = requests.get(f"https://api.agify.io?name={name}", timeout=5)
            elapsed = round((time.time() - start) * 1000, 2)
            data = response.json()
            success = 1 if response.status_code == 200 and "age" in data else 0

            # Sauvegarde en base
            conn = sqlite3.connect('tests.db')
            c = conn.cursor()
            c.execute('''INSERT INTO test_runs 
                (timestamp, name, status_code, response_time, age, count, success)
                VALUES (?, ?, ?, ?, ?, ?, ?)''',
                (datetime.now().isoformat(), name, response.status_code,
                 elapsed, data.get("age"), data.get("count"), success))
            conn.commit()
            conn.close()

            results.append({
                "name": name,
                "status_code": response.status_code,
                "response_time_ms": elapsed,
                "age": data.get("age"),
                "count": data.get("count"),
                "success": success
            })
        except Exception as e:
            results.append({
                "name": name,
                "error": str(e),
                "success": 0
            })

    return jsonify(results)

@app.get("/dashboard")
def dashboard():
    conn = sqlite3.connect('tests.db')
    c = conn.cursor()
    c.execute("SELECT * FROM test_runs ORDER BY id DESC LIMIT 50")
    rows = c.fetchall()
    conn.close()
    return render_template('dashboard.html', rows=rows)

@app.get("/metrics")
def metrics():
    conn = sqlite3.connect('tests.db')
    c = conn.cursor()
    c.execute("SELECT COUNT(*), SUM(success), AVG(response_time) FROM test_runs")
    total, success, avg_time = c.fetchone()
    conn.close()
    return jsonify({
        "total_tests": total,
        "success": success,
        "failed": total - success if total and success else 0,
        "success_rate": round((success / total) * 100, 2) if total and success else 0,
        "avg_response_time_ms": round(avg_time, 2) if avg_time else 0
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
