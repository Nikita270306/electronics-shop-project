from src.phone import Phone
from src.item import Item
import pytest

item = Item("Newphone", 50000, 20)
cool_phone = Phone("iPhone 15 Pro Max", 150000, 5, 10)


class TestPhone:
    def test_for_str(self):
        assert str(cool_phone) == "iPhone 15 Pro Max"

    def test_for_repr(self):
        assert repr(cool_phone) == "Phone('iPhone 15 Pro Max', 150000, 5, 10)"

    def test_adding(self):
        assert item + cool_phone == 25
        assert item + item == 40
        assert cool_phone + cool_phone == 10
        assert cool_phone + item == 25

    def test_for_number_of_sim(self):
        with pytest.raises(ValueError) as error:
            cool_phone.number_of_sim = 0

        assert str(error.value) == "Количество физических SIM-карт должно быть целым числом больше нуля."