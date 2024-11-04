import pytest
from arlotti_es11.es11 import Primo

@pytest.fixture(autouse=True)
def test_primo():
    primo = Primo("Spaghetti alla Carbonara", 20, ["Spaghetti", "Uova", "Pancetta"], "Media", "Spaghetti", "Carbonara")
    assert Primo.sugo == "Carbonara"