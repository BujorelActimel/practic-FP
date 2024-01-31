from domain import Tractor
from repo import Repo
from service import Service

def test_delete_tractors_with_digit_in_price():
    service = Service(Repo("service/test_data_files/test_delete.csv"))
    assert len(service.repo.tractoare) == 3
    service.delete_tractors_with_digit_in_price(3)
    assert len(service.repo.tractoare) == 2
    with open("service/test_data_files/test_delete.csv", "w") as f:
        f.write("id,denumire,pret,model,data\n1,tractor1,100_000,model1,12:1:2024\n2,tractor2,150_000,model2,1:2:2024\n3,tractor3,300_000,model2,2:2:2024")


def test_filter_tractors_by_string_and_price():
    service = Service(Repo("service/test_data_files/test_filter.csv"))
    assert len(service.filter_tractors_by_string_and_price("", -1)) == 3
    assert len(service.filter_tractors_by_string_and_price("tractor", 200_000)) == 2
    assert len(service.filter_tractors_by_string_and_price("tractor3", 200_000)) == 0
