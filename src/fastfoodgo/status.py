ALLOWED_TRANSITIONS = {
    "CREATED": ["PAID"],
    "PAID": ["PREPARING"],
    "PREPARING": ["DELIVERED"],
    "DELIVERED": [],
}


def is_valid_status_transition(current_status: str, new_status: str) -> bool:
    if current_status not in ALLOWED_TRANSITIONS:
        raise ValueError("Unknown current status")

    return new_status in ALLOWED_TRANSITIONS[current_status]
