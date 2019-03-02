from flask import Flask, render_template, redirect, url_for, request, session, flash
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# CONFIG
app.config.from_object(os.environ['APP_SETTINGS'])


db = SQLAlchemy(app)

class showtime(db.Model):
	__tablename__ = 'showtime'
	id = db.Column(db.Integer, primary_key = True)
	showtime = db.Column(db.DateTime)
	location = db.Column(db.String(100))
	comedian = db.Column(db.String(100))
	description = db.Column(db.Text)
	most_recent = db.Column(db.String(20))

@app.route("/")
def index():
	shows=showtime.query.all()
	return render_template("index.html", shows=shows)

if __name__ == "__main__":
	app.run()