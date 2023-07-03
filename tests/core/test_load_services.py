import pandas as pd
import pytest
from sqlalchemy import create_engine, text

from pypdtools.core.services.load_services import LoadToCsv, LoadToSql


@pytest.fixture
def engine():
    """Create a temporary in-memory SQLite database."""
    engine = create_engine("sqlite:///:memory:")
    yield engine
    engine.dispose()


@pytest.fixture
def data():
    """Create a sample DataFrame."""
    data = {
        "name": ["Alice", "Bob", "Charlie"],
        "age": [25, 30, 35],
        "gender": ["F", "M", "M"],
    }
    return pd.DataFrame(data)


def test_load_to_csv_services(tmp_path, data):
    """Test the LoadToCsv class."""
    # Create a CSV file
    path = tmp_path / "test.csv"
    service = LoadToCsv(data, path)
    service.load()

    # Check that the CSV file was created correctly
    result = pd.read_csv(path)
    expected = data
    pd.testing.assert_frame_equal(result, expected)


def test_load_to_sql_services(engine, data):
    """Test the LoadToSql class."""
    # Create a table in the database
    with engine.connect() as con:
        con.execute(text("CREATE TABLE test (name TEXT, age INTEGER, gender TEXT)"))

    # Load the data into the table
    service = LoadToSql(data, engine, "test")
    service.load()

    # Check that the data was loaded correctly
    with engine.connect() as con:
        result = con.execute(text("SELECT * FROM test")).fetchall()
    expected = [("Alice", 25, "F"), ("Bob", 30, "M"), ("Charlie", 35, "M")]
    assert result == expected
