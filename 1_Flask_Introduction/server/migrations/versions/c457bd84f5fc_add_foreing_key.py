"""Add foreing key

Revision ID: c457bd84f5fc
Revises: 7c05b1bcd487
Create Date: 2023-07-03 10:43:11.438916

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c457bd84f5fc'
down_revision = '7c05b1bcd487'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('schedules', schema=None) as batch_op:
        batch_op.create_foreign_key(batch_op.f('fk_schedules_student_id_students'), 'students', ['student_id'], ['id'])

    # ### end Alembic commands ###



def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('schedules', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_schedules_student_id_students'), type_='foreignkey')

    # ### end Alembic commands ###
