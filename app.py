from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta 
import redis
from rejson import Client, Path

rj = Client(host='localhost', port=6379, decode_responses=True)

app = Flask(__name__)
app.secret_key = "123"
app.permanent_session_lifetime = timedelta(minutes = 10)

wsgi_app = app.wsgi_app

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/Magazines")
def magazines():
	return render_template("Mag.html")		


@app.route("/create", methods = ["POST", "GET"])
def create():
	if request.method == 'POST':
		bookID = request.form['bookID'];
		title = request.form['title'];
		authors = request.form['authors'];
		ratings = request.form['ratings'];

		rj.jsonset(bookID, Path.rootPath(),{"title": title,"authors": authors,"average_rating": ratings})
	return render_template("create.html");

@app.route("/view", methods = ["POST", "GET"])
def view():
	if request.method == 'POST':
		bookID = request.form['bookID'];
		book = rj.jsonget(bookID)
		print(book)
		return render_template("view.html", book = book)
	else: 
		return render_template("view.html")


@app.route("/delete", methods = ["POST", "GET"])
def delete():
	if request.method == 'POST':
		bookID = request.form['bookID'];
		rj.jsondel(bookID)
	return render_template("delete.html");


@app.route("/update", methods = ["POST", "GET"])
def update():
	if request.method == 'POST':
		bookID = request.form['bookID'];
		title = request.form['title'];
		authors = request.form['authors'];
		ratings = request.form['ratings'];
		rj.jsonset(bookID, Path('.title'), title)
		rj.jsonset(bookID, Path('.authors'), authors)
		rj.jsonset(bookID, Path('.average_rating'), ratings)
	return render_template("update.html");
	

if __name__ == "__main__":
	import os
	HOST = os.environ.get('SERVER_HOST', 'localhost')
	try:
	    PORT = int(os.environ.get('SERVER_PORT', '5000'))
	except ValueError:
	    PORT = 5000
	app.run(HOST, PORT, debug=True)










