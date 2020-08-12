from slconf import slconf


def test_sample():
    """Sample test."""
    assert slconf.increment(1) == 2
