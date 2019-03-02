from flask import Flask, render_template, redirect, url_for, request, session, flash
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# CONFIG
app.config.from_object(os.environ['APP_SETTINGS'])
#app.config.from_object('config.ProductionConfig')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/laugh_tracker'
#'postgres://yltvamaeksflmr:107bfa9a1e5096f4fe0e9b77fc231ebbcdc238f33e85bcd8a36f2765b6a77fe8@ec2-23-21-244-254.compute-1.amazonaws.com:5432/dc344enjr2hp39'

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