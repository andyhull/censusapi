import os
from database import engine, db_session, init_db
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flask_sqlalchemy import SQLAlchemy

DEBUG = True
SECRET_KEY = 'development key'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/')
def index():
    # cur = db_session.execute('select phone, buddy from numbers order by id desc')
    # cur = Numbers.query.all()
    # app.logger.debug('All numbers: %s' % (cur))

    return render_template('show_entries.html')

if __name__ == '__main__':
    init_db()
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

