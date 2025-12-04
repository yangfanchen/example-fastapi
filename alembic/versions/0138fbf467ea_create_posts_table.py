"""create posts table

Revision ID: 0138fbf467ea
Revises: 
Create Date: 2025-12-02 16:44:28.215060

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0138fbf467ea'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
                    sa.Column('title',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
