import pytest
from analytic import heat_rate, thermal_resistance

def test_known_value():  
    """Test with known values to verify calculation accuracy.""" 
    Q = heat_rate(400.0, 1e-6, 0.5, 300.0, 4.0)
    assert Q == pytest.approx(0.2368)

def test_q_equals_delta_T_over_R():
    """Test that Q = ΔT/R relationship holds."""
    k, A, L = 400.0, 1e-6, 0.5
    R = thermal_resistance(k, A, L)
    Q = heat_rate(k, A, L, 300.0, 4.0)
    assert Q == pytest.approx((300.0 - 4.0) / R)

def test_double_L_halves_Q():
    Q1 = heat_rate(400.0, 1e-6, 0.5, 300.0, 4.0)
    Q2 = heat_rate(400.0, 1e-6, 1.0, 300.0, 4.0)
    assert Q2 == pytest.approx(Q1 / 2)
    
def test_thermal_resistance_calculation():
    """Test thermal resistance calculation with known values."""
    R = thermal_resistance(400.0, 1e-6, 0.5)
    assert R == pytest.approx(1250.0)
