import attr

from viper.db.manager import DBManager
from viper.db.utils import insert, read_all
from viper.models.core import Conv


def test_qry():
    dbmgr = DBManager.make_db_manager(uri="sqlite:///:memory:", readonly=True)

    instr = Conv(id=0, window_size=3, has_bias=True)

    assert insert(dbmgr, data=attr.asdict(instr), tablename="Conv") == 1
    from_db = [Conv(**row) for row in read_all(dbmgr, tablename="Conv")]
    assert [instr] == from_db
