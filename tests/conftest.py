import pytest
import sys
import os
import importlib

sys.path.append(os.path.dirname(__file__))
sys.path.append("scrapers")
sys.path.append("app")


@pytest.fixture(scope="session", autouse=True)
def reload_all_modules():
    for k, v in sys.modules.items():
        if k.startswith("pipeline"):
            importlib.reload(v)
