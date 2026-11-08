# grades.py
def compute_final_grade(prelim, midterm, finals):
    """30% prelim, 30% midterm, 40% finals."""
    for score in (prelim, midterm, finals):
        if not 0 <= score <= 100:
            raise ValueError("Scores must be 0-100")
    return round(prelim * 0.3 + midterm * 0.3
                 + finals * 0.4, 2)

def remark(final_grade):
    if final_grade >= 75:
        return "PASSED"
    return "FAILED"
