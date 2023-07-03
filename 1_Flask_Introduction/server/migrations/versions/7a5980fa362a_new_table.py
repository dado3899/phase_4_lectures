"""new table

Revision ID: 7a5980fa362a
Revises: 64dc362b9e6f
Create Date: 2023-07-03 10:37:03.603030

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a5980fa362a'
down_revision = '64dc362b9e6f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('schedules',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('class_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('schedules')
    # ### end Alembic commands ###
