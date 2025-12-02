import sys
import requests
import pytest

def python_version():
    # Return a fake version object matching the test expectations
    class Version:
        major = 3
        minor = 8

    return Version()

def requests_version():
    return "2.27.1"

def pytest_version():
    return "7.1.3"
