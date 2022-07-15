from payment import payment
from bank import bank

class tranfer(bank, payment):
    def __init__(self, id,typePayment, ammount, bankname, identification, numberAccount, date):
        super().__init__(id, typePayment, ammount, bankname, identification, numberAccount, date)