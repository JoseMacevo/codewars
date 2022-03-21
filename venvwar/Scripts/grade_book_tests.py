from grade_book import get_grade


def test_case_a():
    assert get_grade(95, 90, 93) == "A", "get_grade(95, 90, 93)"
    assert get_grade(100, 85, 96) == "A", "get_grade(100, 85, 96)"
    assert get_grade(92, 93, 94) == "A", "get_grade(92, 93, 94)"
    assert get_grade(100, 100, 100) == "A", "get_grade(100, 100, 100)"
    
    assert get_grade(70, 70, 100) == "B", "get_grade(70, 70, 100)"
    assert get_grade(82, 85, 87) == "B", "get_grade(82, 85, 87"
    assert get_grade(84, 79, 85) == "B", "get_grade(84, 79, 85)"
    
    assert get_grade(70, 70, 70) == "C", "get_grade(70, 70, 70)"
    assert get_grade(75, 70, 79) == "C", "get_grade(75, 70, 79)"
    assert get_grade(60, 82, 76) == "C", "get_grade(60, 82, 76)"
    
    assert get_grade(65, 70, 59) == "D", "get_grade(65, 70, 59)"
    assert get_grade(66, 62, 68) == "D", "get_grade(66, 62, 68)"
    assert get_grade(58, 62, 68) == "D", "get_grade(58, 62, 70)"
    
    assert get_grade(44, 55, 52) == "F", "get_grade(44, 55, 52)"
    assert get_grade(48, 55, 52) == "F", "get_grade(48, 55, 52)"
    assert get_grade(58, 59, 60) == "F", "get_grade(58, 59, 60)"
    assert get_grade(0, 0, 0) == "F", "get_grade(0, 0, 0)"
