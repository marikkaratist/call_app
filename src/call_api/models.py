from sqlalchemy import Table, Column, Integer, String, MetaData

metadata = MetaData()

call = Table(
    'call',
    metadata,
    Column("phone", Integer, nullable=False),
    Column("address", String, nullable=False)
)
