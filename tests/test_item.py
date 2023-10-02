from src.item import Item
import pytest


class Test():
    def test_calculate_total_price(self):
        item = Item("Бананы", 20, 1000)

        assert item.calculate_total_price() == 20000

    def test_apply_discount(self):
        item = Item("Бананы", 20, 1000)

        item.pay_rate = 0.5
        item.apply_discount()
        assert item.price == 10

