import sys
import isbn


def test_equality(actual, expected):
    line_num = sys._getframe(1).f_lineno
    if actual == expected:    
        print(f'Test at line {line_num} OK')
    else:
        print(f'Test at line {line_num} FAILED. Expected {expected} but got {actual}')


def run_tests():
    result_0 = isbn.is_valid('3-598-21508-8')
    test_equality(result_0, True)
    
    result_1 = isbn.is_valid('3-598-21508-7')
    test_equality(result_1, False)
    
    result_1 = isbn.is_valid('3-598-21507-X')
    test_equality(result_1, True)

run_tests()