from flask_appbuilder.security.views import UserDBModelView
from flask_babel import lazy_gettext
from flask_appbuilder.models.sqla.filters import FilterStartsWith, FilterEqualFunction


class MyUserDBModelView(UserDBModelView):
    """
        View that add DB specifics to User view.
        Override to implement your own custom view.
        Then override userdbmodelview property on SecurityManager
    """

    show_fieldsets = [
        (lazy_gettext('User info'),
         {'fields': ['username', 'active', 'roles', 'login_count', 'group', 'main_group']}),
        (lazy_gettext('Personal Info'),
         {'fields': ['first_name', 'last_name', 'email'], 'expanded': True}),
        (lazy_gettext('Audit Info'),
         {'fields': ['last_login', 'fail_login_count', 'created_on',
                     'created_by', 'changed_on', 'changed_by'], 'expanded': False}),
    ]

    user_show_fieldsets = [
        (lazy_gettext('User info'),
         {'fields': ['username', 'active', 'roles', 'login_count', 'group', 'main_group']}),
        (lazy_gettext('Personal Info'),
         {'fields': ['first_name', 'last_name', 'email'], 'expanded': True}),
    ]

    add_columns = ['first_name', 'last_name', 'username', 'active', 'email', 'roles', 'group', 'main_group', 'password', 'conf_password']
    list_columns = ['first_name', 'last_name', 'username', 'email', 'active', 'roles', 'group', 'main_group','shared_with']
    edit_columns = ['first_name', 'last_name', 'username', 'active', 'email', 'roles', 'group', 'main_group']

