"""Initial DB

Revision ID: 50398ad5afac
Revises:
Create Date: 2019-06-24 00:14:51.254371

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '50398ad5afac'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('session',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('uid', sa.Text(), nullable=True),
                    sa.Column('url', sa.Text(), nullable=True),
                    sa.Column('date', sa.Date(), nullable=True),
                    sa.Column('time', sa.Time(), nullable=True),
                    sa.PrimaryKeyConstraint('id', name=op.f('pk_session'))
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('session')
    # ### end Alembic commands ###
