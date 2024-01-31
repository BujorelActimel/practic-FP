from repo import Repo
from domain import Tractor

def test_Repo():
    repo = Repo("repo/test_data_files/test.csv")
    assert len(repo.tractoare) == 3


def test_save_data():
    repo = Repo("repo/test_data_files/test_save.csv")
    repo.tractoare.append(Tractor(1, "tractor1", 100_000, "model1", 12, 1, 2024))
    repo.save_data()
    with open("repo/test_data_files/test_save.csv", "r") as f:
        tractor = f.readlines()[1].strip()
        assert tractor == "1,tractor1,100000,model1,12:1:2024"
    
    with open("repo/test_data_files/test_save.csv", "w") as f:
        f.write("")


def test_add_tractor():
    repo = Repo("repo/test_data_files/test_add.csv")
    try:
        repo.add_tractor(1)
    except ValueError:
        assert True
    else:
        assert False

    repo.add_tractor(Tractor(1, "tractor1", 100_000, "model1", 12, 1, 2024))

    assert len(repo.tractoare) == 1
    with open("repo/test_data_files/test_add.csv", "r") as f:
        tractor = f.readlines()[1].strip()
        assert tractor == "1,tractor1,100000,model1,12:1:2024"

    with open("repo/test_data_files/test_add.csv", "w") as f:
        f.write("")


def test_undo():
    repo = Repo("repo/test_data_files/test_undo.csv")

    repo.add_tractor(Tractor(1, "tractor1", 100_000, "model1", 12, 1, 2024))
    assert len(repo.tractoare) == 1

    repo.undo()
    assert len(repo.tractoare) == 0

    repo.undo()
    assert len(repo.tractoare) == 0

    with open("repo/test_data_files/test_undo.csv", "w") as f:
        f.write("")
