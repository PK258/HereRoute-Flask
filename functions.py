import config
import sqlalchemy
import pandas as pd


def fetchdata(Country, City, Station, FromDirection, FromDistance, ToDirection, ToDistance):
    engn = sqlalchemy.create_engine(config.mysql_ConnectionString)
    FromID = pd.read_sql_query(config.FromID_query, engn, params=(Country, City, Station, FromDirection, FromDistance))
    ToID = pd.read_sql_query(config.ToID_query, engn, params=(Country, City, Station, ToDirection, ToDistance))

    data = pd.read_sql_query(config.FetchData_query, engn, params=(FromID, ToID))

    return data