"""Add User model

Revision ID: 0190a3f46a65
Revises: 
Create Date: 2020-10-18 06:47:20.174127

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0190a3f46a65'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('server',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('server', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_server_id'), ['id'], unique=False)
        batch_op.create_index(batch_op.f('ix_server_name'), ['name'], unique=True)

    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_ops', sa.Boolean(), nullable=True),
    sa.Column('is_superuser', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_user_id'), ['id'], unique=False)

    op.create_table('port',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('num', sa.Integer(), nullable=False),
    sa.Column('internal_num', sa.Integer(), nullable=True),
    sa.Column('server_id', sa.Integer(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['server_id'], ['server.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('num', 'server_id', name='_port_num_server_uc')
    )
    with op.batch_alter_table('port', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_port_id'), ['id'], unique=False)

    op.create_table('server_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('server_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['server_id'], ['server.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('server_user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_server_user_id'), ['id'], unique=False)

    op.create_table('port_forward_rule',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('port_id', sa.Integer(), nullable=True),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('method', sa.String(), nullable=False),
    sa.Column('remote_address', sa.String(), nullable=False),
    sa.Column('remote_port', sa.Integer(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['port_id'], ['port.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('port_forward_rule', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_port_forward_rule_id'), ['id'], unique=False)

    op.create_table('port_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('port_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['port_id'], ['port.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('port_user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_port_user_id'), ['id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('port_user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_port_user_id'))

    op.drop_table('port_user')
    with op.batch_alter_table('port_forward_rule', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_port_forward_rule_id'))

    op.drop_table('port_forward_rule')
    with op.batch_alter_table('server_user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_server_user_id'))

    op.drop_table('server_user')
    with op.batch_alter_table('port', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_port_id'))

    op.drop_table('port')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_id'))
        batch_op.drop_index(batch_op.f('ix_user_email'))

    op.drop_table('user')
    with op.batch_alter_table('server', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_server_name'))
        batch_op.drop_index(batch_op.f('ix_server_id'))

    op.drop_table('server')
    # ### end Alembic commands ###