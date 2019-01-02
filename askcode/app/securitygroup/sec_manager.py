from flask_appbuilder.security.sqla.manager import SecurityManager
from app.securitygroup.sec_user_model import MyUser
from app.securitygroup.sec_user_view import MyUserDBModelView

class MySecurityManager(SecurityManager):
    user_model = MyUser
    userdbmodelview = MyUserDBModelView