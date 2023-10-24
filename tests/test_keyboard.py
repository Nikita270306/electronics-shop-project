
from src.keyboard import Keyboard

keyb_1 = Keyboard("Keyboard_1", 15000, 10)
keyb_2 = Keyboard("Keyboard_2", 10000, 20)


class TestKeyboard:
    def test_for_str(self):
        assert str(keyb_1) == "Keyboard_1"
        assert str(keyb_2) == "Keyboard_2"

    def test_for_repr(self):
        assert repr(keyb_1) == "Keyboard('Keyboard_1', 15000, 10)"
        assert repr(keyb_2) == "Keyboard('Keyboard_2', 10000, 20)"

    def test_for_change_lang(self):
        assert keyb_1._language == "EN"
        assert keyb_2._language == "EN"

        keyb_1.change_lang()
        assert keyb_1._language == "RU"
        keyb_1.change_lang()
        assert keyb_1._language == "EN"

        keyb_2.change_lang()
        assert keyb_2._language == "RU"
        keyb_2.change_lang()
        assert keyb_2._language == "EN"
