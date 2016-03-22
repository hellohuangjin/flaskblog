"""add confirmed field

Revision ID: 1c144f672e46
Revises: 457ee4ce5750
Create Date: 2015-12-28 15:19:46.646000

"""

# revision identifiers, used by Alembic.
revision = '1c144f672e46'
down_revision = '457ee4ce5750'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    ### end Alembic commands ###
