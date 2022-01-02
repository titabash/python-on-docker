import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/../")
"""
Write your module
Ex. import hoge
"""
from api import hello_web  # noqa: E402


def test_is_mainCmd():
    assert hello_web() == "Hello, Python Api!"
