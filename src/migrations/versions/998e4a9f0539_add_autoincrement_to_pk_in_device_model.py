"""Add autoincrement to pk in Device model

Revision ID: 998e4a9f0539
Revises: e171ffc557d5
Create Date: 2024-02-16 23:21:38.035498

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '998e4a9f0539'
down_revision: Union[str, None] = 'e171ffc557d5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
