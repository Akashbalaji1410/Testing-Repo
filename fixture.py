"""Synthetic source fixture for a static-analysis smoke test."""

def check_fixture(value: int) -> int:
    assert value >= 0
    return value
