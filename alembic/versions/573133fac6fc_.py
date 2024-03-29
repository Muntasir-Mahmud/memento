"""empty message

Revision ID: 573133fac6fc
Revises: 171069641dcd
Create Date: 2024-03-09 02:43:43.545843

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '573133fac6fc'
down_revision: Union[str, None] = '171069641dcd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'topics', ['topic_id'])
    op.drop_constraint('topics_parent_topic_id_fkey', 'topics', type_='foreignkey')
    op.drop_column('topics', 'parent_topic_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('topics', sa.Column('parent_topic_id', sa.UUID(), autoincrement=False, nullable=True))
    op.create_foreign_key('topics_parent_topic_id_fkey', 'topics', 'topics', ['parent_topic_id'], ['topic_id'])
    op.drop_constraint(None, 'topics', type_='unique')
    # ### end Alembic commands ###
