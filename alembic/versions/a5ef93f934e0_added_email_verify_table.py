"""added email verify table

Revision ID: a5ef93f934e0
Revises: 701872aa5262
Create Date: 2023-01-24 23:07:11.190528

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5ef93f934e0'
down_revision = '701872aa5262'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('email_verification',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('temp_jwt', sa.String(length=255), nullable=False),
    sa.Column('users_id', sa.Integer(), nullable=False),
    sa.Column('users_email', sa.String(length=100), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['users_email'], ['users.email'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('email_verification')
    # ### end Alembic commands ###
