import pytest
from fastfoodgo.order import calculate_order_total
from decimal import Decimal


def test_calculate_order_total_nominal():
    items = [
        {"price": 8.5, "quantity": 2},
        {"price": 3.0, "quantity": 1},
    ]
    assert calculate_order_total(items) == Decimal("20.0")


def test_calculate_order_total_empty():
    assert calculate_order_total([]) == Decimal("0.00")


def test_calculate_order_total_invalid_quantity():
    items = [{"price": 5.0, "quantity": 0}]
    with pytest.raises(ValueError):
        calculate_order_total(items)
