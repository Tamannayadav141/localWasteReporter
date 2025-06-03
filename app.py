from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Create database and table
def init_db():
    conn = sqlite3.connect('reports.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT,
            address TEXT,
            image_path TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        description = request.form["description"]
        address = request.form["address"]
        image = request.files["image"]
        timestamp = datetime.now().strftime("%d %B %Y, %I:%M %p")


        image_path = ""
        if image and image.filename:
            filename = secure_filename(image.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(image_path)

        conn = sqlite3.connect("reports.db")
        c = conn.cursor()
        c.execute("INSERT INTO reports (description, address, image_path, timestamp) VALUES (?, ?, ?, ?)",
                  (description, address, image_path, timestamp))
        conn.commit()
        conn.close()
        return redirect(url_for("index"))

    conn = sqlite3.connect("reports.db")
    c = conn.cursor()
    c.execute("SELECT * FROM reports ORDER BY id DESC")
    reports = c.fetchall()
    conn.close()

    return render_template("index.html", reports=reports)
@app.route("/delete/<int:report_id>", methods=["POST"])
def delete_report(report_id):
    conn = sqlite3.connect("reports.db")
    c = conn.cursor()

    # Get image path before deleting
    c.execute("SELECT image_path FROM reports WHERE id = ?", (report_id,))
    result = c.fetchone()
    if result and result[0]:
        image_path = result[0]
        if os.path.exists(image_path):
            os.remove(image_path)

    # Delete the report
    c.execute("DELETE FROM reports WHERE id = ?", (report_id,))
    conn.commit()
    conn.close()

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
