import pytest

# test_capitalize.py

def capital_case(x):
    if not isinstance(x, str):
        raise TypeError('Please provide a string argument')
    return x.capitalize()

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore', "Should be Semaphore"

def test_contains_S():
    assert "S" in capital_case('semaphore'), "s not found!" 