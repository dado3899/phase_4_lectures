"""new column

Revision ID: 7c05b1bcd487
Revises: 7a5980fa362a
Create Date: 2023-07-03 10:38:51.619048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c05b1bcd487'
down_revision = '7a5980fa362a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('schedules', schema=None) as batch_op:
        batch_op.add_column(sa.Column('student_id', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('schedules', schema=None) as batch_op:
        batch_op.drop_column('student_id')

    # ### end Alembic commands ###