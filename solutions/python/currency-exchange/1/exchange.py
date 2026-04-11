def exchange_money(budget: float, exchange_rate: float) -> float:
    return budget / exchange_rate


def get_change(budget: float, exchanging_value: float) -> float:
    return budget - exchanging_value


def get_value_of_bills(denomination: int, number_of_bills: int) -> int:
    return denomination * number_of_bills


def get_number_of_bills(amount: float, denomination: int) -> int:
    return int(amount // denomination)


def get_leftover_of_bills(amount: float, denomination: int) -> float:
    return amount % denomination


def exchangeable_value(budget: float, exchange_rate: float, spread: int, denomination: int) -> int:
    effective_rate = exchange_rate * (1 + spread / 100)
    total = budget / effective_rate
    return int(total // denomination * denomination)