from pandastools.abc.scripts import AbstractEtl


def test_extract_not_implemented():
    try:
        etl = AbstractEtl()
        etl.extract()
    except TypeError:
        pass
    else:
        assert False, "Expected TypeError"


def test_transform_not_implemented():
    try:
        etl = AbstractEtl()
        etl.transform()
    except TypeError:
        pass
    else:
        assert False, "Expected TypeError"


def test_load_not_implemented():
    try:
        etl = AbstractEtl()
        etl.load()
    except TypeError:
        pass
    else:
        assert False, "Expected TypeError"


def test_execute_not_implemented():
    try:
        etl = AbstractEtl()
        etl.execute()
    except TypeError:
        pass
    else:
        assert False, "Expected TypeError"
