"""user_sec_group

Revision ID: 64cc9e3fc030
Revises: 869b675add4c
Create Date: 2019-01-01 09:21:11.899109

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64cc9e3fc030'
down_revision = '869b675add4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('company')
    op.add_column('ab_user', sa.Column('group', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ab_user', 'group')
    op.create_table('company',
    sa.Column('created_on', sa.DATETIME(), nullable=False),
    sa.Column('changed_on', sa.DATETIME(), nullable=False),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=False),
    sa.Column('created_by_fk', sa.INTEGER(), nullable=False),
    sa.Column('changed_by_fk', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['changed_by_fk'], ['ab_user.id'], ),
    sa.ForeignKeyConstraint(['created_by_fk'], ['ab_user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###
