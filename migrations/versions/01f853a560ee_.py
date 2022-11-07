"""empty message

Revision ID: 01f853a560ee
Revises: c769eba86e68
Create Date: 2022-11-07 12:02:01.469792

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01f853a560ee'
down_revision = 'c769eba86e68'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('survey_question', sa.Column('question', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('survey_question', 'question')
    # ### end Alembic commands ###
