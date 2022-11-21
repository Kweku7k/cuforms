"""empty message

Revision ID: a14829a07cc0
Revises: 01f853a560ee
Create Date: 2022-11-08 09:11:08.246095

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a14829a07cc0'
down_revision = '01f853a560ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('responses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('formId', sa.String(), nullable=True),
    sa.Column('response', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('responses')
    # ### end Alembic commands ###