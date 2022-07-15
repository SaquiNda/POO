from payment import payment

class cash(payment):
    def __init__(self, id, ammount, date, typePayment):
        super().__init__(id, ammount, date, typePayment)