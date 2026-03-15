from flask import Flask, request, jsonify
from database import connect_db, create_table
from log_analyzer import analyze_logs

app = Flask(__name__)

create_table()

@app.route("/add_log", methods=["POST"])
def add_log():

    data = request.json

    service = data["service"]
    level = data["level"]
    message = data["message"]

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO logs(service,level,message) VALUES(?,?,?)",
        (service, level, message)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Log added"})


@app.route("/logs")
def get_logs():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM logs")
    logs = cursor.fetchall()

    conn.close()

    return jsonify(logs)


@app.route("/analyze")
def analyze():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM logs")
    logs = cursor.fetchall()

    conn.close()

    result = analyze_logs(logs)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)