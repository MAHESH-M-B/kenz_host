"""empty message

Revision ID: c84b78db1f9b
Revises: 3c64d519c9cb
Create Date: 2023-04-03 10:39:17.958609

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c84b78db1f9b'
down_revision = '3c64d519c9cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('delivery_time', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('delivery_type', sa.String(length=100), nullable=True))

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_wholesale', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('is_wholesale')

    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.drop_column('delivery_type')
        batch_op.drop_column('delivery_time')

    # ### end Alembic commands ###