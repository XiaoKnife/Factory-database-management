"""empty message

Revision ID: c7a8fcb1124f
Revises: 51e70afee758
Create Date: 2019-12-16 20:40:13.972138

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7a8fcb1124f'
down_revision = '51e70afee758'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('order_ibfk_1', 'order', type_='foreignkey')
    op.create_foreign_key(None, 'order', 'cooperation', ['company'], ['company'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'order', type_='foreignkey')
    op.create_foreign_key('order_ibfk_1', 'order', 'cooperation', ['company'], ['company'])
    # ### end Alembic commands ###
