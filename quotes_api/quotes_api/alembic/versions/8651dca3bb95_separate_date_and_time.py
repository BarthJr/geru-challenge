"""Separate date and time

Revision ID: 8651dca3bb95
Revises: 17155e239338
Create Date: 2019-06-17 19:32:56.034091

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '8651dca3bb95'
down_revision = '17155e239338'
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