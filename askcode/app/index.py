from flask_appbuilder import IndexView
from flask import request, app, current_app



class SubdomainIndex(IndexView):
    index_template = 'v_index.html'