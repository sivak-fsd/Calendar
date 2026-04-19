from flask import Flask, render_template, jsonify, request
from datetime import datetime, date
import calendar

app = Flask(__name__, template_folder="../templates", static_folder="../static")


@app.route("/")
def index():
    today = date.today()
    return render_template("index.html", year=today.year, month=today.month)


@app.route("/api/calendar/<int:year>/<int:month>")
def get_calendar(year, month):
    cal = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]
    return jsonify({
        "year": year,
        "month": month,
        "month_name": month_name,
        "weeks": cal,
        "today": date.today().isoformat(),
    })


if __name__ == "__main__":
    app.run(debug=True)
