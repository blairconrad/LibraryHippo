"""Add User model

Revision ID: 950253b23e42
Revises: b2fc8df2f32f
Create Date: 2020-04-13 06:34:24.894890

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '950253b23e42'
down_revision = 'b2fc8df2f32f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('social_id', sa.String(length=64), nullable=False),
    sa.Column('nickname', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('social_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###