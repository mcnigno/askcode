import logging
from flask import Flask, request
from flask_appbuilder import SQLA, AppBuilder, IndexView, BaseView
from flask_migrate import Migrate
#from app.views import SubdomainIndex
from app.index import SubdomainIndex
from app.securitygroup.sec_manager import MySecurityManager


"""
 Logging configuration
"""

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)
# solve parso vs Ipython parso log problem
logging.getLogger('parso.python.diff').disabled = True
logging.getLogger('parso.cache').disabled=True
logging.getLogger('parso.cache.pickle').disabled=True


app = Flask(__name__)


app.config.from_object('config')
db = SQLA(app)
migrate = Migrate(app, db)




appbuilder = AppBuilder(app, db.session,
                indexview=SubdomainIndex, 
                base_template='my_base.html',
                security_manager_class=MySecurityManager)


"""
from sqlalchemy.engine import Engine
from sqlalchemy import event

#Only include this for SQLLite constraints
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    # Will force sqllite contraint foreign keys
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
"""    

from app import views, models


