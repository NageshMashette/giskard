"""create table feedback replies

Revision ID: 81808bd4049a
Revises: 5b74a912e6cc
Create Date: 2021-09-27 08:22:15.832918

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81808bd4049a'
down_revision = '5b74a912e6cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('feedback_replies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('feedback_id', sa.Integer(), nullable=False),
    sa.Column('reply_to_reply', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(), nullable=True),
    sa.Column('created_on', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['feedback_id'], ['feedbacks.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['reply_to_reply'], ['feedback_replies.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_feedback_replies_feedback_id'), 'feedback_replies', ['feedback_id'], unique=False)
    op.create_index(op.f('ix_feedback_replies_id'), 'feedback_replies', ['id'], unique=False)
    op.create_index(op.f('ix_feedback_replies_reply_to_reply'), 'feedback_replies', ['reply_to_reply'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_feedback_replies_reply_to_reply'), table_name='feedback_replies')
    op.drop_index(op.f('ix_feedback_replies_id'), table_name='feedback_replies')
    op.drop_index(op.f('ix_feedback_replies_feedback_id'), table_name='feedback_replies')
    op.drop_table('feedback_replies')
    # ### end Alembic commands ###
