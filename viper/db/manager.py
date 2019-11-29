import sqlalchemy as sa
import attr

from viper.utils.misc import itersubclasses
from viper.db.utils import SQLBase

# Importing all models to activate the subclassing of SQLBase
from viper import models  # noqa


@attr.s(auto_attribs=True, kw_only=True, frozen=True)
class DBManager:
    uri: str
    engine: sa.engine.Engine
    conn: sa.engine.Connection
    meta: sa.MetaData
    readonly: bool

    @classmethod
    def make_db_manager(
        cls, *, uri: str, readonly: bool = False, echo: bool = False
    ) -> "DBManager":
        engine = sa.create_engine(uri, echo=echo)
        meta = sa.MetaData()
        conn = engine.connect()
        init_tables(meta, engine)

        return cls(uri=uri, engine=engine, conn=conn, meta=meta, readonly=readonly)

    def __getitem__(self, item):
        return self.meta.tables[item]


def init_tables(meta, engine):
    table_classes = list(itersubclasses(SQLBase))
    for table_cls in table_classes:
        table_cls.make_table(meta)
    meta.create_all(engine)
