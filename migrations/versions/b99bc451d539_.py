"""empty message

Revision ID: b99bc451d539
Revises: 270fc4d1c74d
Create Date: 2023-03-11 15:56:34.285615

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b99bc451d539'
down_revision = '270fc4d1c74d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('propertytable', schema=None) as batch_op:
        batch_op.drop_column('photo')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('propertytable', schema=None) as batch_op:
        batch_op.add_column(sa.Column('photo', postgresql.BYTEA(), autoincrement=False, nullable=False))

    # ### end Alembic commands ###
