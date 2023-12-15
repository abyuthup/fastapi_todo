"""create phone number for user column

Revision ID: fda7c72ebaae
Revises: 
Create Date: 2023-12-15 22:33:55.293726

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fda7c72ebaae'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users',sa.Column('phone_number',sa.String(50), nullable=True))


def downgrade() -> None:
    op.drop_column('users','phone_number')
