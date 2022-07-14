from payment import payment
from bank import bank

class tranfer(payment, bank):
    def __init__(self, id, ammount, bank, identification, numberAccount):
        super().__init__(id, ammount, bank, identification, numberAccount)