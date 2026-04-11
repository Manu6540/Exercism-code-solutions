def is_criticality_balanced(temperature: float, neutrons_emitted: float) -> bool:
    return (
        temperature < 800 and
        neutrons_emitted > 500 and
        temperature * neutrons_emitted < 500000
    )


def reactor_efficiency(voltage: float, current: float, theoretical_max_power: float) -> str:
    efficiency = (voltage * current) / theoretical_max_power * 100

    if efficiency >= 80:
        return "green"
    elif efficiency >= 60:
        return "orange"
    elif efficiency >= 30:
        return "red"
    else:
        return "black"


def fail_safe(temperature: float, neutrons_produced_per_second: float, threshold: float) -> str:
    value = temperature * neutrons_produced_per_second

    if value < 0.9 * threshold:
        return "LOW"
    elif value <= 1.1 * threshold:
        return "NORMAL"
    else:
        return "DANGER"