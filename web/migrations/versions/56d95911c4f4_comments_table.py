"""comments table

Revision ID: 56d95911c4f4
Revises: 
Create Date: 2018-09-11 00:29:50.653740

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56d95911c4f4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ip', sa.String(length=64), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('comment', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comment_ip'), 'comment', ['ip'], unique=False)
    op.create_index(op.f('ix_comment_timestamp'), 'comment', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_comment_timestamp'), table_name='comment')
    op.drop_index(op.f('ix_comment_ip'), table_name='comment')
    op.drop_table('comment')
    # ### end Alembic commands ###