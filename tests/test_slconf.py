from slconf import slconf


def test_sample():
    assert slconf.increment(1) == 2
