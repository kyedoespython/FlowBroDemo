from flask import Flask
from flask_sqlalchemy import SQLAlchemy  
from flask_migrate import Migrate
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash
from werkzeug.security import  check_password_hash

import os

load_dotenv()

# initialise extensions
db = SQLAlchemy()
migrate = Migrate()

class User_Accounts(db.Model):
    __tablename__ = "Users"
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

class Data_Sets(db.Model):
    __tablename__ = "Data"
    data_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("Users.user_id"), nullable=False)
    title = db.Column(db.String(225), nullable=False)
    description = db.Column(db.String(640), nullable=False)
    file_type = db.Column(db.String(32), nullable=False) # csv, excel(xlsx), sqlite
    original_file_name = db.Column(db.String(255), nullable=False)
    stored_file_name = db.Column(db.String(255), nullable=False, unique=True) # uuid based
    file_byte_size = db.Column(db.Integer, nullable=False)
    upload_date = db.Column(db.DateTime, server_default=db.func.now()) # timestampt

