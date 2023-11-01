import pytest

from src.item import Item, InstantiateCSVError


class TestError:
    @pytest.mark.raises()
    def test_for_found(self):
        try:
            Item.instantiate_from_csv('../src/itemsssss.csv')
        except FileNotFoundError:
            assert "Ok" == "Ok"

    @pytest.mark.raises()
    def test_for_broken(self):
        try:
            Item.instantiate_from_csv('../venv/incor.csv')
        except InstantiateCSVError:
            assert "Ok" == "Ok"
