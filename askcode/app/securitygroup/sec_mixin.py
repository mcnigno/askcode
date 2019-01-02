import datetime
import logging

from sqlalchemy import Column, Integer, ForeignKey, DateTime, String, Sequence, UniqueConstraint, Table
from sqlalchemy.orm import relationship
import sqlalchemy.types as types
from sqlalchemy.ext.declarative import declared_attr
from flask_appbuilder.models.sqla.filters import FilterStartsWith, FilterEqualFunction, FilterInFunction, FilterRelationManyToManyEqual
from flask_appbuilder import ModelView, BaseView, Model
from .sec_user_model import Group


from flask import g

log = logging.getLogger(__name__)

def my_groups():
    list_g = [str(x) for x in g.user.group]
    
    return list_g



class SecView(ModelView):
    
    base_filters = [['group', FilterInFunction, my_groups],
                    #['repo_doc_group', FilterRelationManyToManyEqual, Group] 
                    ]
    
    
    

class SecMixin(object):
    
    @declared_attr
    def repo_doc_group(cls):
        assoc_doc_group = Table('repo_doc_group', Model.metadata, 
                                  Column('id', Integer, Sequence('doc_group_id_seq'), primary_key=True),
                                  Column('type',String(30), default=cls.__name__),
                                  Column('doc_id', Integer, ForeignKey(str(cls.__name__).lower() + '.id')),
                                  Column('group_id', Integer, ForeignKey('group.id')),
                                  UniqueConstraint('doc_id', 'group_id') 
)
        return relationship('Group', secondary=assoc_doc_group, backref=cls.__name__)
 
    @declared_attr
    def main_group_id(cls):

        return Column(Integer,ForeignKey('group.id'),
                    default=cls.get_main_group_id,
                    onupdate=cls.get_main_group_id, 
                    nullable=False)
    
    @declared_attr
    def main_group(cls):

        return relationship("Group", primaryjoin='%s.main_group_id == Group.id' % cls.__name__, enable_typechecks=False)

    '''
    @declared_attr
    def main_group(cls):
        return Column(String(50), ForeignKey('ab_user.id'),
                      default=cls.get_main_group, onupdate=cls.get_main_group, nullable=False)
    '''
    @classmethod
    def get_main_group(cls):
        try:
            return str(g.user.main_group)
        except Exception as e:
            return None
    
    @classmethod
    def get_main_group_id(cls):
        try:
            return int(g.user.main_group_id)
        except Exception as e:
            return None
    """
        AuditMixin
        Mixin for models, adds 4 columns to stamp, time and user on creation and modification
        will create the following columns:
        
        :created on:
        :changed on:
        :created by:
        :changed by:
    

    created_on = Column(DateTime, default=datetime.datetime.now, nullable=False)
    changed_on = Column(DateTime, default=datetime.datetime.now,
                        onupdate=datetime.datetime.now, nullable=False)

    

    @declared_attr
    def created_by(cls):
        return relationship("User", primaryjoin='%s.created_by_fk == User.id' % cls.__name__, enable_typechecks=False)

    @declared_attr
    def changed_by_fk(cls):
        return Column(Integer, ForeignKey('ab_user.id'),
                      default=cls.get_user_id, onupdate=cls.get_user_id, nullable=False)

    @declared_attr
    def changed_by(cls):
        return relationship("User", primaryjoin='%s.changed_by_fk == User.id' % cls.__name__, enable_typechecks=False)

    @classmethod
    def get_user_id(cls):
        try:
            return g.user.id
        except Exception as e:
            # log.warning("AuditMixin Get User ID {0}".format(str(e)))
            return None
    """