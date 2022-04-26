import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "79no45etgve485i7tygvbd5ir87etygvbegrtyi8udb5ekt5iyudgbv"

    MONGODB_SETTINGS = { 'db' : 'SPS_Enrolment' }