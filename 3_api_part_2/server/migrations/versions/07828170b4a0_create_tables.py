"""Create tables

Revision ID: 07828170b4a0
Revises: 
Create Date: 2024-08-07 10:08:15.810192

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07828170b4a0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chefs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('specialty', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_chefs'))
    )
    op.create_table('pastries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('moisture_content', sa.Integer(), nullable=True),
    sa.Column('country_of_origin', sa.String(), nullable=True),
    sa.Column('chef_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['chef_id'], ['chefs.id'], name=op.f('fk_pastries_chef_id_chefs')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_pastries'))
    )
    op.create_table('ingredients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.Column('measurement_type', sa.String(), nullable=True),
    sa.Column('pastry_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['pastry_id'], ['pastries.id'], name=op.f('fk_ingredients_pastry_id_pastries')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_ingredients'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ingredients')
    op.drop_table('pastries')
    op.drop_table('chefs')
    # ### end Alembic commands ###