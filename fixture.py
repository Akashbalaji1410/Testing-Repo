"""Synthetic static-analysis fixture. No credentials or external services."""

import hashlib

# Random text generated for the Gitleaks generic API key rule.
# It has never been issued by a provider or used for authentication.
api_key = "d3aec1b82ac5353070d41fec463130fc3c05561bdb46794e"


def check_fixture(value: int) -> int:
    assert value >= 0
    return value


def public_sample_fingerprint() -> str:
    """Use a public constant to exercise weak-hash review rules."""
    return hashlib.md5(b"public scanner fixture").hexdigest()
