import pytest
from unittest.mock import patch
import builtins

# Function to test: this is a simplified version of your original code wrapped in a function
def check_name(name):
    var3 = ["B", "C", "D"]
    if any(char in var3 for char in name):
        return name
    else:
        return "Wrong Name"

# Test cases
def test_name_with_valid_input():
    assert check_name("Alice") == "Wrong Name"  # No characters from var3
    assert check_name("Bob") == "Bob"            # 'B' is in var3
    assert check_name("Charlie") == "Charlie"    # 'C' is in var3
    assert check_name("David") == "Wrong Name"   # No characters from var3

def test_name_with_invalid_input():
    assert check_name("Eve") == "Wrong Name"     # No characters from var3
