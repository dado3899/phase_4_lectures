"""Added students and related FK

Revision ID: 13954030e2a3
Revises: f86ef9e379bc
Create Date: 2024-04-23 11:29:35.514502

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13954030e2a3'
down_revision = 'f86ef9e379bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('grade', sa.Float(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_students'))
    )
    with op.batch_alter_table('lectures', schema=None) as batch_op:
        batch_op.add_column(sa.Column('student_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_lectures_student_id_students'), 'students', ['student_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('lectures', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_lectures_student_id_students'), type_='foreignkey')
        batch_op.drop_column('student_id')

    op.drop_table('students')
    # ### end Alembic commands ###
