"""testing parameters on users table

Revision ID: 7dabb53a6ab1
Revises: bad1c1d5ef85
Create Date: 2024-09-03 17:54:14.600967

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7dabb53a6ab1'
down_revision: Union[str, None] = 'bad1c1d5ef85'
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
