"""backbone and immuno

Revision ID: 2c61bfbf51aa
Revises:
Create Date: 2015-02-28 18:23:33.611889

"""

# revision identifiers, used by Alembic.
revision = '2c61bfbf51aa'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('backbone',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Unicode(length=10), nullable=False),
    sa.Column('flanks3_s', sa.Unicode(length=80), nullable=False),
    sa.Column('flanks3_a', sa.Unicode(length=80), nullable=False),
    sa.Column('flanks5_s', sa.Unicode(length=80), nullable=False),
    sa.Column('flanks5_a', sa.Unicode(length=80), nullable=False),
    sa.Column('loop_s', sa.Unicode(length=30), nullable=False),
    sa.Column('loop_a', sa.Unicode(length=30), nullable=False),
    sa.Column('miRNA_s', sa.Unicode(length=30), nullable=False),
    sa.Column('miRNA_a', sa.Unicode(length=30), nullable=False),
    sa.Column('miRNA_length', sa.Integer(), nullable=False),
    sa.Column('miRNA_min', sa.Integer(), nullable=False),
    sa.Column('miRNA_max', sa.Integer(), nullable=False),
    sa.Column('miRNA_end_5', sa.Integer(), nullable=False),
    sa.Column('miRNA_end_3', sa.Integer(), nullable=False),
    sa.Column('structure', sa.Unicode(length=200), nullable=False),
    sa.Column('homogeneity', sa.Integer(), nullable=False),
    sa.Column('miRBase_link', sa.Unicode(length=200), nullable=False),
    sa.Column('active_strand', sa.Integer(), nullable=False),
    sa.Column('regexp', sa.Unicode(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('input_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('transcript_name', sa.Unicode(length=20), nullable=False),
    sa.Column('minimum_CG', sa.Integer(), nullable=False),
    sa.Column('maximum_CG', sa.Integer(), nullable=False),
    sa.Column('maximum_offtarget', sa.Integer(), nullable=False),
    sa.Column('scaffold', sa.Unicode(length=10), nullable=True),
    sa.Column('immunostimulatory', sa.Unicode(length=15), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('immuno',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sequence', sa.Unicode(length=10), nullable=False),
    sa.Column('receptor', sa.Unicode(length=15), nullable=True),
    sa.Column('link', sa.Unicode(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('result',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('shmir', sa.Unicode(length=300), nullable=False),
    sa.Column('score', postgresql.JSON(), nullable=False),
    sa.Column('pdf', sa.Unicode(length=150), nullable=False),
    sa.Column('sequence', sa.Unicode(length=30), nullable=False),
    sa.Column('backbone', sa.Integer(), nullable=True),
    sa.Column('input_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['backbone'], [u'backbone.id'], ),
    sa.ForeignKeyConstraint(['input_id'], ['input_data.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('result')
    op.drop_table('immuno')
    op.drop_table('input_data')
    op.drop_table('backbone')
    ### end Alembic commands ###
