"""empty message

Revision ID: 5bdb29fea440
Revises: 53bc1531e512
Create Date: 2023-04-07 13:56:09.325013

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5bdb29fea440'
down_revision = '53bc1531e512'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.alter_column('status',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.Enum('ORDERED', 'ORDER_PROCESSING', 'OUT_FOR_DELIVERY', 'DELIVERED', name='orderstatus'),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.alter_column('status',
               existing_type=sa.Enum('ORDERED', 'ORDER_PROCESSING', 'OUT_FOR_DELIVERY', 'DELIVERED', name='orderstatus'),
               type_=sa.VARCHAR(length=100),
               existing_nullable=False)

    # ### end Alembic commands ###