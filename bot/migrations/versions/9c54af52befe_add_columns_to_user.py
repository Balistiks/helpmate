"""add columns to User

Revision ID: 9c54af52befe
Revises: c922e4291f10
Create Date: 2023-11-18 18:59:34.319043

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9c54af52befe'
down_revision: Union[str, None] = 'c922e4291f10'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
