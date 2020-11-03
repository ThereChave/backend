"""Make config default as empty dict

Revision ID: 839d89c468af
Revises: 9640520863ca
Create Date: 2020-10-31 23:58:41.604381

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import sqlite

# revision identifiers, used by Alembic.
revision = '839d89c468af'
down_revision = '9640520863ca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('port_forward_rule', schema=None) as batch_op:
        batch_op.alter_column('config',
               existing_type=sqlite.JSON(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('port_forward_rule', schema=None) as batch_op:
        batch_op.alter_column('config',
               existing_type=sqlite.JSON(),
               nullable=True)

    # ### end Alembic commands ###