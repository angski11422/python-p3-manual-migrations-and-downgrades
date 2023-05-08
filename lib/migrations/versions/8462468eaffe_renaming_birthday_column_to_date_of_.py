"""Renaming birthday column to date_of_birth

Revision ID: 8462468eaffe
Revises: 791279dd0760
Create Date: 2023-05-07 19:52:23.530174

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8462468eaffe'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'birthday', new_column_name='date_of_birth')


def downgrade() -> None:
    op.alter_column('students', 'date_of_birth', new_column_name='birthday')
