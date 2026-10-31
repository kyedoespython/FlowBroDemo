from flask import Flask # basic web server client
from sqlalchemy.engine import URL
from db_init.db import db
from db_init.db import migrate
from flask import render_template # render in html pages
from flask import request # grab useful data via html
from flask import flash # display messages via html
from flask import redirect # redirect to pages
from flask import jsonify # return usable data
from flask import session # track users across pages after login
from werkzeug.utils import secure_filename # secure filename uploads
from werkzeug.exceptions import RequestEntityTooLarge # error handle for large files

import os
import urllib.parse
import csv
import io

app = Flask(__name__)

# postgresql url settings via (.env)
db_url = URL.create(
    drivername="postgresql+psycopg",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT", 8080)),
    database=os.getenv("DB_NAME"),
)

app.config["SQLALCHEMY_DATABASE_URI"] = db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# File upload settings
MAX_UPLOAD_MB = int(os.environ.get('MAX_UPLOAD_MB', 16))
app.config['MAX_CONTENT_LENGTH'] = MAX_UPLOAD_MB * 1024 * 1024

# load database config + migrate
db.init_app(app)
migrate.init_app(app, db)

@app.route("/")
def home():
    return render_template("dashboard.html")

@app.route("/Join_Us", methods=["POST"])
def Join_Us():
    return render_template("Join_Us.html")

@app.route("/handle_Join_Request")
def Handle_Join():
    request.form.get("username")
    request

@app.route("/Login")
def Login_Page():
    return render_template("Login.html")

# Playground
@app.route("/Playground")
def Playground():
    return render_template("playground.html")

# handle file input sizes
@app.errorhandler(RequestEntityTooLarge)
def handle_large_files():
    return jsonify({
        "error": f"File size too large, Max size allowed is {MAX_UPLOAD_MB}MB",
        "max_size_mb": MAX_UPLOAD_MB
    }), 413