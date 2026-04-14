def value_of_card(card: str) -> int:
    """Return the value of a single card."""
    if card in ["J", "Q", "K"]:
        return 10
    elif card == "A":
        return 1
    else:
        return int(card)


def higher_card(card_one: str, card_two: str):
    """Return the card with higher value, or both if equal."""
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if value_one > value_two:
        return card_one
    elif value_two > value_one:
        return card_two
    else:
        return card_one, card_two


def value_of_ace(card_one: str, card_two: str) -> int:
    """Return best value (1 or 11) for an Ace."""
    
    # If already an Ace is present, next Ace = 1
    if card_one == "A" or card_two == "A":
        return 1

    total = value_of_card(card_one) + value_of_card(card_two)

    if total + 11 <= 21:
        return 11
    else:
        return 1


def is_blackjack(card_one: str, card_two: str) -> bool:
    """Check if hand is a blackjack (Ace + 10 card)."""
    return (
        (card_one == "A" and value_of_card(card_two) == 10) or
        (card_two == "A" and value_of_card(card_one) == 10)
    )


def can_split_pairs(card_one: str, card_two: str) -> bool:
    """Check if cards can be split into pairs."""
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one: str, card_two: str) -> bool:
    """Check if hand total allows double down (9–11)."""
    total_value = value_of_card(card_one) + value_of_card(card_two)
    return 9 <= total_value <= 11