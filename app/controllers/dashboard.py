import sys
import traceback
from app import app, db, models, helpers
from flask import render_template

@app.route('/')
def main():
	seasons = helpers.get_seasons()
	# print('seasons:', seasons)
	return render_template('index.html', seasons=seasons)
