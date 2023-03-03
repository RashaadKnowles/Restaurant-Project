from pasta import Pasta
from pizza import Pizza
from salad import Salad
class OrderFactory:
    def __init__(self) -> None:
        pass

    @staticmethod
    def create_order(type):
        if type == 'Pasta':
            return Pasta()
        elif type == 'Pizza':
            return Pizza()
        elif type == 'Salad':
            return Salad()