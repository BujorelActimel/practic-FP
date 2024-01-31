from datetime import date
from domain import Tractor

def test_Tractor():
    tractor = Tractor(1, "tractor1", 100_000, "model-x", 13, 2, 2024)

    assert tractor.ID == 1
    assert tractor.denumire == "tractor1"
    assert tractor.pret == 100_000
    assert tractor.model == "model-x"
    assert tractor.data == date(2024, 2, 13)
