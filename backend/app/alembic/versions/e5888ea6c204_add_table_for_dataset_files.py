"""Add table for dataset files

Revision ID: e5888ea6c204
Revises: 7a9ee66421fc
Create Date: 2021-04-19 08:21:04.434049

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e5888ea6c204"
down_revision = "7a9ee66421fc"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "datasets",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("file_name", sa.String(), nullable=False),
        sa.Column("location", sa.String(), nullable=False),
        sa.Column("owner_id", sa.Integer(), nullable=False),
        sa.Column("project_id", sa.Integer(), nullable=False),
        sa.Column("created_on", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["owner_id"],
            ["user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["project_id"],
            ["projects.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_datasets_file_name"), "datasets", ["file_name"], unique=False
    )
    op.create_index(op.f("ix_datasets_id"), "datasets", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_datasets_id"), table_name="datasets")
    op.drop_index(op.f("ix_datasets_file_name"), table_name="datasets")
    op.drop_table("datasets")
    # ### end Alembic commands ###
