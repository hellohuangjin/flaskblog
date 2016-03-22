"""passworld

Revision ID: 101de838998e
Revises: 18618dc37a9a
Create Date: 2015-12-15 18:24:48.708000

"""

# revision identifiers, used by Alembic.
revision = '101de838998e'
down_revision = '18618dc37a9a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=128), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password_hash')
    ### end Alembic commands ###
