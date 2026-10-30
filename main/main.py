import sqlite3
import os

from create_account.account import check_valid_db as db_check
from create_account.account import check_for_user as check_user_exists

class db_init:
    # check if database exists already, creates it if it doesn't
    db_check()
    check_user_exists()


init = db_init()