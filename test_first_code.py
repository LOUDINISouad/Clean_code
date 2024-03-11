import pytest

from first_code import get_area

def test_get_area():
    # test circle
    radius = 5
    expected_area = 3.14159 * radius**2
    assert get_area("circle", radius=radius) == expected_area

    # test square
    width = 4
    expected_area = width**2
    assert get_area("square", width=width) == expected_area

    # test rectangle
    width = 3
    height = 6
    expected_area = width * height
    assert get_area("rectangle", width=width, height=height) == expected_area

    # test invalid
    with pytest.raises(ValueError):
        assert get_area("invalid_shape") == None
