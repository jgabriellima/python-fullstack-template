from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import datetime
sample_page = Blueprint('sample_page', 'sample_page', template_folder='templates', static_folder='static')

@sample_page.route('/')
def home():
    try:
        return render_template('index.html') #str(datetime.datetime.now()) #
    except TemplateNotFound:
        abort(404)
        
        
@sample_page.route('/sample')
def get_sample():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)
        