import pytest

from src.item import Item


class TestError:
    @pytest.mark.raises()
    def test_for_found(self):
        Item.instantiate_from_csv('../src/itemsssss.csv')

    @pytest.mark.raises()
    def test_for_broken(self):
        Item.instantiate_from_csv('../src/my_error/item_wrong.csv')