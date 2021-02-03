from flask import Blueprint, render_template, abort, redirect
from jinja2 import TemplateNotFound
import datetime
sample_page = Blueprint('sample_page', 'sample_page', template_folder='templates', static_folder='static')

@sample_page.route('/')
def home():
    try:
        return render_template('index.html') #str(datetime.datetime.now()) #
    except TemplateNotFound:
        abort(404)
        

@sample_page.errorhandler(404)   
def not_found(e):   
  return render_template('index.html')

@sample_page.route('/', defaults={'path': ''})
@sample_page.route('/<path:path>')
def catch_all(path):
    return sample_page.send_static_file("index.html")

@sample_page.route('/sample')
def get_sample():
    try:
        return redirect('index.html/#/about')
    except TemplateNotFound:
        abort(404)
        