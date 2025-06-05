from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base

# Definición de metadata para cada conjunto de tablas
metadata_alarmas = MetaData()
BaseAlarmas = declarative_base(metadata=metadata_alarmas)

metadata_estrategias = MetaData()
BaseEstrategias = declarative_base(metadata=metadata_estrategias)

metadata_diary = MetaData()
BaseDiary = declarative_base(metadata=metadata_diary)

metadata_positions = MetaData()
BasePositions = declarative_base(metadata=metadata_positions)

metadata_accounts = MetaData()
BaseAccounts = declarative_base(metadata=metadata_accounts)

metadata_kline_data = MetaData()
BaseKLineData = declarative_base(metadata=metadata_kline_data)

metadata_orders = MetaData()
BaseOrders = declarative_base(metadata=metadata_orders)
