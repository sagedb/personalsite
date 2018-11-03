from flask import Flask, render_template, url_for, request, flash, redirect, send_from_directory
from flask_pymongo import PyMongo
import pymongo  #document-oriented database
import urllib  # in coordination with an RFC
import json
from bson import ObjectId
from werkzeug import secure_filename
import os

app = Flask(__name__, static_url_path='/static')


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)
