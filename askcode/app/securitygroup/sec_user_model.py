from flask_appbuilder.security.sqla.models import User
from sqlalchemy import Column, Integer, ForeignKey, String, Sequence, Table, UniqueConstraint
from sqlalchemy.orm import relationship, backref
from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin


class Group(AuditMixin, Model):
    id = Column(Integer, primary_key=True)
    
    name = Column(String(256))
    user_id = Column(Integer, ForeignKey('ab_user.id'))
    

    def __repr__(self):
        return self.name

assoc_user_group = Table('ab_user_group', Model.metadata,
                                  Column('id', Integer, Sequence('ab_user_group_id_seq'), primary_key=True),
                                  Column('user_id', Integer, ForeignKey('ab_user.id')),
                                  Column('group_id', Integer, ForeignKey('group.id')),
                                  UniqueConstraint('user_id', 'group_id')
)

class MyUser(User):
    __tablename__ = 'ab_user'
    main_group_id = Column(Integer, ForeignKey('group.id'))
    main_group = relationship('Group', foreign_keys=[main_group_id])
    group = relationship('Group', secondary=assoc_user_group, backref='user')

    
    
    


