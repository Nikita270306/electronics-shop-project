
class InstantiateCSVError(Exception):
    def __init__(self, message="Файл items.csv поврежден"):
        super().__init__(message)
