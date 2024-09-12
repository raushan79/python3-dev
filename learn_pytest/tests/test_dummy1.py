import sys
import os
import pytest

# Adjust sys.path to include the project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import module
from mycodes.dummy_code1 import add


def test_add():
    assert add(1, 2) == 3
