# for alembic
pip install alembic


# init alembic
alembic init <alembic env name> ie , alembic init alembic


# add database path to alembic.ini
sqlalchemy.url = mysql+pymysql://root:1425mysql#@127.0.0.1:3306/TodoApplicationDatabase

# import our models to alembic/env.py
import models


# delete line 'if config.config_file_name is not None:' from env.py


# set 'target_metadata = None' to
target_metadata = models.Base.metadata



# create alembic revision of what change we gonna make in database
alembic revision -m "create phone number for user column"

# write upgrade function alembic/versions folder
def upgade() -> None:
    op.add_column('users',sa.Column('phone_number',sa.String(50), nullable=True))

# call upgade alembic revision
alembic upgrade <revisionId>
alembic upgrade fda7c72ebaae

# add phone_number to user model
phone_number = Column(String)

