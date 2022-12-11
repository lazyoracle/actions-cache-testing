import numpy as np

def test_muddy():
    x = [1e-5, 1e-3, 1e-1]
    y = np.arccos(np.cos(x))
    np.testing.assert_allclose(x, y, rtol=1e-5, atol=0)

def test_muddy_2():
    x = [1e-5, 1e-3, 1e-1]
    y = np.arccos(np.cos(x))
    np.testing.assert_allclose(x, y, rtol=1e-5, atol=0)
