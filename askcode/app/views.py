from flask import render_template, request, redirect
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, BaseView, expose, IndexView, action
from app import appbuilder, db
from app.securitygroup.sec_user_model import Group
from .models import Company
from flask_appbuilder.models.sqla.filters import FilterStartsWith, FilterEqualFunction, FilterInFunction
from app.securitygroup.sec_mixin import SecView

class GroupView(ModelView):
    datamodel = SQLAInterface(Group)

"""
    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(MyModelView, "My View", icon="fa-folder-open-o", category="My Category", category_icon='fa-envelope')
"""
from flask import g



class CompanyView(SecView):
    datamodel = SQLAInterface(Company)
    list_columns = ['created_by','name','group', 'main_group','repo_doc_group']
    base_filters = []
    add_columns = ['name']
    edit_columns = ['name','group', 'main_group','repo_doc_group']
    @action("myaction","Do something on this record","Do you really want to?","fa-rocket")
    def myaction(self, item):
        
        print(self.base_filters)
        """
            do something with the item record
        """
        return redirect(self.get_redirect())
    
    
    


class MyView(BaseView):
    route_base = "/"
    @expose('/method1/<string:param1>')
    def method1(self, param1):
        # do something with param1
        # and return it
        subdomain = str(request.url_root).split('//')[1].split('.')[0]
        
        print('subdomain:', subdomain)
        return param1

class domain(BaseView):
    #app = current_app._get_current_object()
    #request = app.request_started

    route_base = '/domain'
    @expose('/method1/<string:param1>')
    def method1(self, param1):
        # do something with param1
        # and return it
        return param1
    
    @expose('/method3/<string:param1>')
    
    #@has_access
    def method3(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        subdomain = str(request).split('//')[1].split('.')[0]
        #subdomain = 'eggs'
        template = subdomain + '_index.html'
        self.update_redirect()
        return self.render_template(template,
                            param1 = param1)
    '''
    if request:
        request = request.url_root  
    else:
        request = 'https://plus.example.com'
    
    subdomain = str(request).split('//')[1].split('.')[0]
    #subdomain = 'eggs'
    template = subdomain + '_index.html'
    '''
appbuilder.add_view_no_menu(domain)
appbuilder.add_link("Method3", href='/myview/method3/john', category='My View')

appbuilder.add_view_no_menu(MyView)

appbuilder.add_view(GroupView, "Group", icon="fa-folder-open-o", category="Security", category_icon='fa-envelope')
appbuilder.add_view(CompanyView, "Group", icon="fa-folder-open-o", category="Menu", category_icon='fa-envelope')


"""
    Application wide 404 error handler
"""
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404

db.create_all()


