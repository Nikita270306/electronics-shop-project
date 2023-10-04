from src.item import Item
import pytest

item = Item("Бананы", 20, 1000)
item1 = Item("TV", 200000, 10)

class Test():
    def test_calculate_total_price(self):
        assert item.calculate_total_price() == 20000

    def test_apply_discount(self):

        item.pay_rate = 0.5
        item.apply_discount()
        assert item.price == 10

    def test_instantiate_from_csv(self):
        assert item1.name == "TV"
        item1.name = "telephone"
        assert item1.name == "telephone"

        Item.instantiate_from_csv("../src/items.csv")
        assert len(Item.all) == 7
        assert Item.all[3].price == 1000
        assert Item.all[5].quantity == 5
    def test_string_to_number(self):
        assert Item.string_to_number('5') == 5
        assert Item.string_to_number('5.0') == 5
        assert Item.string_to_number('5.5') == 5
        assert Item.string_to_number('3401.67584') == 3401
