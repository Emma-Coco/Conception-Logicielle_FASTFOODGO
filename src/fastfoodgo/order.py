from decimal import Decimal


def calculate_order_total(items: list[dict]) -> Decimal:
    if not items:
        return Decimal("0.00")

    total = Decimal("0.00")

    for item in items:
        price = Decimal(str(item["price"]))
        quantity = item["quantity"]

        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        total += price * quantity

    return total
