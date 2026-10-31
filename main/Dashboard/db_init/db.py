from flask import Flask
from flask_sqlalchemy import SQLAlchemy  
from flask_migrate import Migrate
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash
from werkzeug.security import  check_password_hash
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base

import os

load_dotenv()

# initialise extensions
db = SQLAlchemy()
migrate = Migrate()
Base = declarative_base()

# table for storing user accounts and status
class User_Accounts(db.Model):
    __tablename__ = "Users"
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    verified_account = db.Column(bool, default=False, nullable=False)
    time_verified = db.Column(DateTime(timezone=True, server_default=func.now()))

# table for storing raw data and connect the data to the user
class Data_Sets(db.Model):
    __tablename__ = "Data"
    data_id = db.Column(db.Integer, primary_key=True) # store data via id

    # back refference user_id to a data_id
    user_id = db.Column(db.Integer, db.ForeignKey("Users.user_id"), nullable=False)

    # columns for data blocks
    data_title = db.Column(db.String(225), nullable=False)
    data_description = db.Column(db.String(640), nullable=False)
    data_file_type = db.Column(db.String(32), nullable=False) # csv, excel(xlsx), sqlite
    original_file_name = db.Column(db.String(255), nullable=False)
    stored_file_name = db.Column(db.String(255), nullable=False, unique=True) # uuid based
    file_byte_size = db.Column(db.Integer, nullable=False)
    total_mb_uploaded = db.Column(db.String(255), nullable=False)
    upload_date = db.Column(db.DateTime, server_default=db.func.now()) # timestampt

# table for storing client build configs
class Builds(db.Model):
    __tablename__ = "Builds"
    build_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("Users.user_id"), nullable=False)
    build_name = db.Column(db.String(64), nullable=False, unique=True)
    build_description = db.Column(db.String(255), nullable=False, unique=True)
    file_type = db.Column(db.String(64), nullable=False)

class Build_Queries(db.Model):
    __tablename__ = "Build_Queries"
    query_id = db.Column(db.Integer, primary_key=True)
    query_name = db.Column(db.String(64), unique=True, nullable=False)
    query_description = db.Column(db.String(255), unique=True, nullable=False)
    query_performed = db.Column(db.String(255), nullable=False)