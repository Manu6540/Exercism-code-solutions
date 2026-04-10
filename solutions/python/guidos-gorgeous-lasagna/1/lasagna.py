# Task 1: Constant
EXPECTED_BAKE_TIME = 40


# Task 2: Remaining bake time
def bake_time_remaining(elapsed_bake_time):
    """Calculate remaining bake time.

    :param elapsed_bake_time: int - minutes already baked
    :return: int - remaining bake time
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


# Task 3: Preparation time
def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time.

    :param number_of_layers: int - number of layers
    :return: int - preparation time in minutes
    """
    return number_of_layers * 2


# Task 4: Total elapsed time
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - number of layers in the lasagna
    :param elapsed_bake_time: int - time already baked
    :return: int - total time (prep + baking)

    This function calculates total time spent cooking.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time