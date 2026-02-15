"""
Pytest configuration. Sets Django test settings so tests run with SQLite.
"""
import os


def pytest_configure(config):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "opc.settings_test")
