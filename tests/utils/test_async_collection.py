import asyncio

import pytest

from pypdtools.utils.asyncs import AsyncCollection


@pytest.fixture
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def collection():
    return [1, 2, 3, 4, 5]


@pytest.fixture
def async_collection(collection):
    return AsyncCollection(collection)


@pytest.mark.anyio
async def test_async_iteration(async_collection):
    async for item in async_collection:
        assert item in async_collection.collection


@pytest.mark.anyio
async def test_async_map(async_collection):
    async def square(x):
        await asyncio.sleep(0.1)
        return x * x

    results = await async_collection.map(square)

    assert len(results) == len(async_collection.collection)
    for i, item in enumerate(async_collection.collection):
        assert results[i] == item * item
