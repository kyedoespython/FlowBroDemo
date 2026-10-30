from flask import Flask # basic web server client
from flask import render_template # render in html pages
from flask import request # grab useful data via html
from flask import flash # display messages via html
from flask import redirect # redirect to pages
from flask import jsonify # return usable data
from flask import session # track users across pages after login

from werkzeug.utils import secure_filename # secure filename uploads
from werkzeug.exceptions import RequestEntityTooLarge # error handle for large files

import os
import hashlib
import csv
import io

# app configs
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-fallback")

# File upload settings
MAX_UPLOAD_MB = int(os.environ.get('MAX_UPLOAD_MB', 16))
app.config['MAX_CONTENT_LENGTH'] = MAX_UPLOAD_MB * 1024 * 1024

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