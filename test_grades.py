# test_grades.py
import pytest

from grades import compute_final_grade, remark


def test_typical_scores():
    prelim, midterm, finals = 80, 85, 90
    result = compute_final_grade(prelim, midterm, finals)
    assert result == pytest.approx(85.5)


# NORMAL VALUES (expected values worked out by hand)
@pytest.mark.parametrize(
    "prelim, midterm, finals, expected",
    [
        (70, 70, 70, 70.0),      # 21 + 21 + 28
        (90, 80, 70, 79.0),      # 27 + 24 + 28
        (60, 75, 90, 76.5),      # 18 + 22.5 + 36
        (100, 50, 0, 45.0),      # 30 + 15 + 0
    ],
)
def test_normal_values(prelim, midterm, finals, expected):
    assert compute_final_grade(prelim, midterm, finals) == pytest.approx(expected)


# ZERO AND 100
def test_all_zero():
    assert compute_final_grade(0, 0, 0) == pytest.approx(0.0)


def test_all_hundred():
    assert compute_final_grade(100, 100, 100) == pytest.approx(100.0)


# THE PASSING BOUNDARY (remark)
@pytest.mark.parametrize(
    "grade, expected",
    [
        (74.99, "FAILED"),
        (75, "PASSED"),
        (75.01, "PASSED"),
        (0, "FAILED"),
        (100, "PASSED"),
    ],
)
def test_remark_boundary(grade, expected):
    assert remark(grade) == expected


# INVALID SCORES - each position, below 0 and above 100
@pytest.mark.parametrize(
    "prelim, midterm, finals",
    [
        (-1, 80, 80),
        (101, 80, 80),
        (80, -1, 80),
        (80, 101, 80),
        (80, 80, -1),
        (80, 80, 101),
    ],
)
def test_invalid_scores_raise(prelim, midterm, finals):
    with pytest.raises(ValueError):
        compute_final_grade(prelim, midterm, finals)


# ROUNDING to 2 decimals
def test_rounds_to_two_decimals():
    assert compute_final_grade(83.33, 83.33, 83.33) == 83.33
    assert compute_final_grade(77.777, 0, 0) == 23.33


# END-TO-END: grade -> remark
def test_grade_then_remark():
    assert remark(compute_final_grade(60, 75, 90)) == "PASSED"   # 76.5
    assert remark(compute_final_grade(70, 70, 70)) == "FAILED"   # 70.0

def test_failing_grade_remark():
    assert remark(compute_final_grade(50, 60, 70)) == "FAILED"   # 15 + 18 + 28 = 61    