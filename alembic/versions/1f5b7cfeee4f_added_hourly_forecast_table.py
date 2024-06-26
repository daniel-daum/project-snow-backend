"""added hourly forecast table

Revision ID: 1f5b7cfeee4f
Revises: 608d971cb7e6
Create Date: 2023-01-21 11:39:42.007234

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f5b7cfeee4f'
down_revision = '608d971cb7e6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hourly_forecast',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('resort_id', sa.Integer(), nullable=False),
    sa.Column('period', sa.Integer(), nullable=False),
    sa.Column('relative_date', sa.String(length=50), nullable=True),
    sa.Column('start_time', sa.Date(), nullable=False),
    sa.Column('end_time', sa.Date(), nullable=False),
    sa.Column('is_daytime', sa.Boolean(), nullable=True),
    sa.Column('temperature', sa.Integer(), nullable=True),
    sa.Column('temperature_unit', sa.String(length=1), nullable=True),
    sa.Column('temperature_trend', sa.String(length=255), nullable=True),
    sa.Column('wind_speed', sa.String(length=100), nullable=True),
    sa.Column('wind_direction', sa.String(length=5), nullable=True),
    sa.Column('icon', sa.String(), nullable=True),
    sa.Column('short_forecast', sa.String(length=50), nullable=True),
    sa.Column('detailed_forecast', sa.String(length=100), nullable=True),
    sa.Column('last_updated_at', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.Column('valid_from', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.Column('valid_to', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['resort_id'], ['resorts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hourly_forecast')
    # ### end Alembic commands ###
