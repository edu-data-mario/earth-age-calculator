import earth_age_calculator.earth as our_earth


def test_calculate_earth_age():
    assert our_earth.calculate_earth_age(2023) == 4550000000 + (2023 - 1956)
