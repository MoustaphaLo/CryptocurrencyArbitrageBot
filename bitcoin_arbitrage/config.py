import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
#Put My Coinbase SECRET_KEY
SECRET_KEY = '6z4(cg5#3f*ng+xmyu^5l!f)@-h%mwns0rr!c)7!n82sv)upc^'
DEBUG = True

LAST_SPREADS_FILENAME = 'last_spreads.csv'
SPREAD_HISTORY_FILENAME = 'spread_history.csv'
