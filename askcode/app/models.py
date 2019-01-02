from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.orm import relationship, backref
from flask_appbuilder.security.sqla.models import User
from app.securitygroup.sec_mixin import SecMixin


"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""

class Company(AuditMixin,SecMixin,  Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable=False)
    group = Column(String(50))
    
    def __repr__(self):
        return self.name


class Document(AuditMixin,SecMixin,  Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable=False)
    
    
    def __repr__(self):
        return self.name