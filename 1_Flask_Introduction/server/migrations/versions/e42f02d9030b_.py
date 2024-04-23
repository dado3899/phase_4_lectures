"""empty message

Revision ID: e42f02d9030b
Revises: 42d067c49c16
Create Date: 2024-04-22 11:16:28.936534

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e42f02d9030b'
down_revision = '42d067c49c16'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('yoyos', schema=None) as batch_op:
        batch_op.alter_column('era',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('yoyos', schema=None) as batch_op:
        batch_op.alter_column('era',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###