import csv
from src.personal_error.csv_error import InstantiateCSVError

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"

    def __add__(self, other):
        from src.phone import Phone
        if isinstance(self.__class__, Item.__class__):
            return self.quantity + other.quantity
        elif isinstance(self.__class__, Phone.__class__):
            return self.quantity + other.quantity
        raise TypeError("Увы, нельзя сложить Phone или Item с экземплярами не Phone или Item классов!!!!")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_string):
        self.__name = name_string[:10]

    @classmethod
    def instantiate_from_csv(cls, path):
        Item.all.clear()
        with open(path) as f:
            reader = csv.DictReader(f)
            for i in reader:
                cls(i["name"], int(i["price"]), int(i["quantity"]))

    @staticmethod
    def string_to_number(str_):
        return int(float(str_))

    @classmethod
    def instantiate_from_csv(cls, path='../src/items.csv'):
        try:
            with open(path, encoding='utf8') as file:
                checker = csv.DictReader(file)
            try:
                for line in checker:
                    name, price, quantity = line['name'], line['price'], line['quantity']
                    cls(name, price, quantity)
            except InstantiateCSVError:
                raise InstantiateCSVError("C файлом что-то не то")
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл")
        else:
            return "Инициализация экземпляров класса прошла успешно!"
