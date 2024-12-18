"""changed from Users to User

Revision ID: 1907f017a30f
Revises: 69e704b84bc1
Create Date: 2024-11-02 12:28:49.906107

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '1907f017a30f'
down_revision = '69e704b84bc1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('user_id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('password_expiry_dt_tm', sa.DateTime(), nullable=True),
    sa.Column('name_first', sa.String(length=200), nullable=True),
    sa.Column('name_first_key', sa.String(length=100), nullable=True),
    sa.Column('name_full_formatted', sa.String(length=100), nullable=True),
    sa.Column('name_last', sa.String(length=200), nullable=True),
    sa.Column('name_last_key', sa.String(length=100), nullable=True),
    sa.Column('name_middle', sa.String(length=200), nullable=True),
    sa.Column('name_middle_key', sa.String(length=100), nullable=True),
    sa.Column('active_status_cd', sa.BigInteger(), nullable=True),
    sa.Column('active_status_dt_tm', sa.DateTime(), nullable=True),
    sa.Column('active_status_prsnl_id', sa.BigInteger(), nullable=True),
    sa.Column('beg_effective_dt_tm', sa.DateTime(), nullable=True),
    sa.Column('end_effective_dt_tm', sa.DateTime(), nullable=True),
    sa.Column('create_dt_tm', sa.DateTime(), nullable=True),
    sa.Column('create_prsnl_id', sa.BigInteger(), nullable=True),
    sa.Column('updt_applctx', sa.BigInteger(), nullable=True),
    sa.Column('updt_cnt', sa.Integer(), nullable=True),
    sa.Column('updt_dt_tm', sa.DateTime(), nullable=True),
    sa.Column('updt_id', sa.BigInteger(), nullable=True),
    sa.Column('updt_task', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_user_name_first_key'), ['name_first_key'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_name_middle_key'), ['name_middle_key'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_password'), ['password'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index('ix_users_email')
        batch_op.drop_index('ix_users_name_first_key')
        batch_op.drop_index('ix_users_name_middle_key')
        batch_op.drop_index('ix_users_password')
        batch_op.drop_index('ix_users_username')

    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('user_id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(length=128), autoincrement=False, nullable=False),
    sa.Column('password_expiry_dt_tm', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('name_first', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('name_first_key', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('name_full_formatted', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('name_last', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('name_last_key', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('name_middle', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('name_middle_key', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('active_status_cd', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('active_status_dt_tm', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('active_status_prsnl_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('beg_effective_dt_tm', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('end_effective_dt_tm', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('create_dt_tm', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('create_prsnl_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('updt_applctx', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('updt_cnt', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('updt_dt_tm', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updt_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('updt_task', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('user_id', name='users_pkey')
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_index('ix_users_username', ['username'], unique=True)
        batch_op.create_index('ix_users_password', ['password'], unique=False)
        batch_op.create_index('ix_users_name_middle_key', ['name_middle_key'], unique=False)
        batch_op.create_index('ix_users_name_first_key', ['name_first_key'], unique=False)
        batch_op.create_index('ix_users_email', ['email'], unique=True)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))
        batch_op.drop_index(batch_op.f('ix_user_password'))
        batch_op.drop_index(batch_op.f('ix_user_name_middle_key'))
        batch_op.drop_index(batch_op.f('ix_user_name_first_key'))
        batch_op.drop_index(batch_op.f('ix_user_email'))

    op.drop_table('user')
    # ### end Alembic commands ###
