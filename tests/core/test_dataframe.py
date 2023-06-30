from asyncio import ensure_future, gather, sleep

import pandas as pd
import pytest

from pypdtools.core.dataframe import PtDataFrame


def dummy_df():
    """
    Returns a dummy DataFrame.

    Returns:
        pd.DataFrame: A dummy DataFrame.
    """
    return pd.DataFrame(
        {
            "a": [1, 2, 3],
            "b": [4, 5, 6],
            "c": [7, 8, 9],
        }
    )


def test_pt_dataframe():
    """
    Test PtDataFrame initialization.
    """
    df = dummy_df()
    pt_df = PtDataFrame(df)
    assert isinstance(pt_df, PtDataFrame)


def test_forward_iter():
    """
    Test forward iteration over PtDataFrame.
    """
    df = dummy_df()
    pt_df = PtDataFrame(df)

    assert pt_df._iterator.__next__() == (1, 4, 7)
    assert pt_df._iterator.__next__() == (2, 5, 8)
    assert pt_df._iterator.__next__() == (3, 6, 9)


@pytest.mark.anyio
async def test_async_forward_iter():
    """
    Test asynchronous forward iteration over PtDataFrame.
    """
    df = dummy_df()
    pt_df = PtDataFrame(df)

    async for row in pt_df:
        assert row == (1, 4, 7)
        break


def test_with_statement():
    """
    Test PtDataFrame usage within a 'with' statement.
    """
    df = dummy_df()
    pt_df = PtDataFrame(df)

    with pt_df as df:
        assert isinstance(df, pd.DataFrame)


@pytest.mark.anyio
async def test_async_with_statement():
    """
    Test asynchronous PtDataFrame usage within a 'with' statement.
    """
    df = dummy_df()
    pt_df = PtDataFrame(df)

    async with pt_df as df:
        assert isinstance(df, pd.DataFrame)


def test_add():
    """
    Test PtDataFrame addition.
    """
    df = dummy_df()
    pt_df = PtDataFrame(df)
    pt_df2 = PtDataFrame(df)

    pt_df3 = pt_df + pt_df2
    assert isinstance(pt_df3, PtDataFrame)
    assert len(pt_df3) == 6


def test_iadd():
    """
    Test in-place addition of PtDataFrame.
    """
    df = dummy_df()
    pt_df = PtDataFrame(df)
    pt_df2 = PtDataFrame(df)

    pt_df += pt_df2
    assert isinstance(pt_df, PtDataFrame)
    assert len(pt_df) == 6


def test_len():
    """
    Test length calculation of PtDataFrame.
    """
    df = dummy_df()
    pt_df = PtDataFrame(df)

    assert len(pt_df) == 3


def test_repr():
    """
    Test string representation of PtDataFrame.
    """
    df = dummy_df()
    pt_df = PtDataFrame(df)

    assert repr(pt_df) == "   a  b  c\n0  1  4  7\n1  2  5  8\n2  3  6  9"


def test_str():
    """
    Test string representation of PtDataFrame.
    """
    df = dummy_df()
    pt_df = PtDataFrame(df)

    assert str(pt_df) == "   a  b  c\n0  1  4  7\n1  2  5  8\n2  3  6  9"


def test_reduce():
    """
        Test reduction of PtDataFrame objects

    .
    """
    df = dummy_df()
    pt_df = PtDataFrame(df)
    pt_df2 = PtDataFrame(df)

    pt_df3 = PtDataFrame.reduce([pt_df, pt_df2])
    assert isinstance(pt_df3, PtDataFrame)
    assert len(pt_df3) == 6


@pytest.mark.anyio
async def test_gather():
    """
    Test gathering and reduction of PtDataFrame objects asynchronously.
    """
    df = dummy_df()
    ensure1 = ensure_future(sleep(0.0001, PtDataFrame(df)))
    ensure2 = ensure_future(sleep(0.0001, PtDataFrame(df)))
    ensure3 = ensure_future(sleep(0.0001, PtDataFrame(df)))

    df_list = await gather(ensure1, ensure2, ensure3)
    pt_df4 = PtDataFrame.reduce(df_list)
    assert isinstance(pt_df4, PtDataFrame)
    assert len(pt_df4) == 9


def test_col_to_list():
    """
    Test extraction of a column as a list from PtDataFrame.
    """
    df = dummy_df()
    pt_df = PtDataFrame(df)

    assert pt_df.col_to_list("a") == [1, 2, 3]
