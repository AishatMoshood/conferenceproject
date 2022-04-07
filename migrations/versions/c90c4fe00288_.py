"""empty message

Revision ID: c90c4fe00288
Revises: 
Create Date: 2022-04-07 11:08:57.828372

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c90c4fe00288'
down_revision = None
branch_labels = None
depends_on = None


def upgrade(): #updates changes made to db
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lga')
    # ### end Alembic commands ###


def downgrade(): #wont update changes made to db
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lga',
    sa.Column('lga_id', mysql.INTEGER(display_width=10, unsigned=True), autoincrement=True, nullable=False),
    sa.Column('state_id', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('lga_name', mysql.VARCHAR(length=50), server_default=sa.text("''"), nullable=False),
    sa.PrimaryKeyConstraint('lga_id'),
    mysql_default_charset='utf8',
    mysql_engine='MyISAM'
    )
    # ### end Alembic commands ###