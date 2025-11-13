from pytest import approx
import pytest

def test_water_column_height(tower_height, tank_height):
    from water_flow.py import water_column_height

    assert water_column_height(0, 25.0, 48.3) == approx()

def test_pressure_loss_from_pipe(pressure_gain_from_height):
    from water_flow.py import pressure_loss_from_pipe



# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])