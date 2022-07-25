"""empty message

Revision ID: 7cd9da8abae8
Revises: 57a03d098b8c
Create Date: 2022-07-05 13:16:50.086969

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7cd9da8abae8'
down_revision = '57a03d098b8c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('component', sa.String(), nullable=True))
    op.add_column('user', sa.Column('answers', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'answers')
    op.drop_column('question', 'component')
    # ### end Alembic commands ###
