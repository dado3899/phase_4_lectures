"""empty message

Revision ID: 42d067c49c16
Revises: 78ab4800a10e
Create Date: 2024-04-22 11:11:03.587338

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42d067c49c16'
down_revision = '78ab4800a10e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('yoyos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('era', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('yoyos', schema=None) as batch_op:
        batch_op.drop_column('era')

    # ### end Alembic commands ###
