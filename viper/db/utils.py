import sqlalchemy as sa
from typing import Mapping
from abc import ABC, abstractmethod


class SQLBase(ABC):
    @abstractmethod
    def make_table(self, meta):
        pass


def insert(dbmgr, *, data: Mapping, tablename: str) -> int:
    table = dbmgr[tablename]
    qry = sa.insert(table).values(data)
    result = dbmgr.conn.execute(qry)
    num_inserted = result.rowcount
    return num_inserted


def read_all(dbmgr, *, tablename: str) -> int:
    table = dbmgr[tablename]
    qry = table.select()
    result = dbmgr.conn.execute(qry).fetchall()
    return result
