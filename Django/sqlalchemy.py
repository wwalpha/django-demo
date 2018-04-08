from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base

from manage import DATABASES

# SQLAlchemy
ENGINE = create_engine(
    'mysql://%s:%s@%s:%s/%s' % (
        DATABASES['default']['USER'],
        DATABASES['default']['PASSWORD'],
        DATABASES['default']['HOST'],
        DATABASES['default']['PORT'],
        DATABASES['default']['NAME'],
    ),
    echo=True
)

metadata = MetaData()
metadata.reflect(ENGINE)

Base = automap_base(metadata=metadata)
Base.prepare()

Hotel = Base.classes.hotel

# Sessionの作成
session = scoped_session(sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=ENGINE
))
