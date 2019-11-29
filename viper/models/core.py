import attr
import sqlalchemy as sa

from viper.db.utils import SQLBase


@attr.s(auto_attribs=True, kw_only=True, frozen=True)
class Conv(SQLBase):
    id: int
    window_size: int
    has_bias: bool

    @staticmethod
    def make_table(meta):
        return sa.Table(
            "Conv",
            meta,
            sa.Column("id", sa.Integer, primary_key=True),
            sa.Column("window_size", sa.Integer, nullable=False),
            sa.Column("has_bias", sa.Boolean, nullable=False),
        )
