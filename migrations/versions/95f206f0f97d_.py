"""empty message

Revision ID: 95f206f0f97d
Revises: c84b78db1f9b
Create Date: 2023-04-03 20:24:21.152392

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95f206f0f97d'
down_revision = 'c84b78db1f9b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('coupons', schema=None) as batch_op:
        batch_op.drop_column('price_reduction')

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('document_url1', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('document_url2', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('document_url2')
        batch_op.drop_column('document_url1')

    with op.batch_alter_table('coupons', schema=None) as batch_op:
        batch_op.add_column(sa.Column('price_reduction', sa.FLOAT(), nullable=False))

    # ### end Alembic commands ###