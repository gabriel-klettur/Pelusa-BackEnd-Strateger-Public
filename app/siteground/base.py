# Path: app/siteground/base.py

from sqlalchemy.ext.declarative import declarative_base

# Base for alarms database
BaseAlarmas = declarative_base()

# Base for strategies database
BaseEstrategias = declarative_base()

# Base for diary database
BaseDiary = declarative_base()

# Base for positions database
BasePositions = declarative_base()

# Base for accounts database
BaseAccounts = declarative_base()

# Base for k-line data in database
BaseKLineData = declarative_base()

# Base for orders database
BaseOrders = declarative_base()