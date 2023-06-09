"""empty message

Revision ID: 3d6d42570480
Revises: 
Create Date: 2023-04-01 14:14:16.594180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d6d42570480'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('coupons',
    sa.Column('coupon_id', sa.Integer(), nullable=False),
    sa.Column('coupon_name', sa.String(length=50), nullable=False),
    sa.Column('coupon_code', sa.String(length=20), nullable=False),
    sa.Column('reduction_amount', sa.Float(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('active_status', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('price_reduction', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('coupon_id'),
    sa.UniqueConstraint('coupon_code')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('coupons')
    # ### end Alembic commands ###
