"""Add columns to table

Revision ID: 6b9c8e8a6d5a
Revises: 67f5d67aea55
Create Date: 2024-01-12 12:08:22.252897

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b9c8e8a6d5a'
down_revision = '67f5d67aea55'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('price', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('plants')
    # ### end Alembic commands ###
