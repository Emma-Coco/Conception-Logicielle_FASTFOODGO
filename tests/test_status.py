import pytest
from fastfoodgo.status import is_valid_status_transition


def test_valid_transition():
    assert is_valid_status_transition("CREATED", "PAID") is True


def test_invalid_transition():
    assert is_valid_status_transition("CREATED", "DELIVERED") is False


def test_unknown_status():
    with pytest.raises(ValueError):
        is_valid_status_transition("UNKNOWN", "PAID")
