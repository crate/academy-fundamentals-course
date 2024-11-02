import time

import pytest
from cratedb_toolkit.util import DatabaseAdapter


@pytest.fixture()
def cratedb() -> DatabaseAdapter:
    return DatabaseAdapter(dburi="crate://crate@localhost:4200")


@pytest.fixture(scope="function", autouse=True)
def reset_database(cratedb):
    """
    Reset database tables.
    """

    # timeseries_data.ipynb
    cratedb.run_sql("DROP TABLE IF EXISTS weather_data;")
    cratedb.run_sql("DROP TABLE IF EXISTS weather_stations;")

    # multi_model_data.ipynb and full_text_and_vector_search.ipynb
    cratedb.run_sql("DROP TABLE IF EXISTS community_areas;")
    cratedb.run_sql("DROP TABLE IF EXISTS three_eleven_calls;")
    cratedb.run_sql("DROP TABLE IF EXISTS libraries;")

    time.sleep(0.01)
